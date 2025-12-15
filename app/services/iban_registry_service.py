import pandas as pd

from fastapi import UploadFile, File, Depends

from ..db.iban_registry_mongo_repository import IbanRegistryMongoRepository

from .iban_registry_mapper import IBANRegistryMapper

from ..model.iban_registry import (
    IBANRegistry,
    IBANRegistryElement,
    IBANRegistryBBAN,
    IBANRegistryIBAN,
    IBANRegistryContactDetails,
    IBANRegistryUpdates,
    IBANRegistryContact,
)
from ..model.upload_iban_registry_result import UploadIBANRegistryResult

from ..core.domain_exception import DomainException
from ..core.settings import settings
import io


class IBANRegistryService:

    def __init__(
        self,
        iban_registry_repository: IbanRegistryMongoRepository = Depends(),
        iban_registry_mapper: IBANRegistryMapper = Depends(),
    ):

        self.iban_registry_repository = iban_registry_repository

        self.iban_registry_mapper = iban_registry_mapper

    """
    Validate the columns of the record Data element of the registry
    """

    def validate_data_element(self, data: dict):

        REQUIRED_FIELDS = settings.iban_registry_config_header

        if "Data element" not in data:

            raise DomainException(
                "Archivo no valido  , no se encontro la fila Data element"
            )

        values = [v for v in data["Data element"].values() if v not in ("", None)]

        if len(values) != len(REQUIRED_FIELDS):

            raise DomainException(
                f"El número de columnas del Data element es invalido. "
                f"Esperado: {len(REQUIRED_FIELDS)}, recibido: {len(values)}."
            )

        for expected, actual in zip(REQUIRED_FIELDS, values):

            if actual != expected:

                raise DomainException(
                    f"Columna Data element invalida :  '{expected}' pero se recibió '{actual}'."
                )

        return

    """
    Upload the IBAN Registry int txt format provided by swift with the ISO 13616 standard
    """

    def upload_registry(self, file: UploadFile = File(...)) -> UploadIBANRegistryResult:

        df = None

        for encoding in settings.iban_registry_config_encoding:

            try:

                df = pd.read_csv(
                    io.StringIO(file.file.read().decode(encoding)),
                    sep="\t",
                    keep_default_na=False,
                )

                break

            except UnicodeDecodeError:

                continue

        if df is None:
            raise DomainException(
                "Does not possible to read the file, check the encoding"
            )

        iban_registry_dict = df.to_dict("dict")

        self.validate_data_element(iban_registry_dict)

        iban_registry_list = self.iban_registry_mapper.map_dict_to_iban_registry_list(
            iban_registry_dict
        )

        self.iban_registry_repository.delete_all()

        records_saved = self.iban_registry_repository.save(iban_registry_list)

        return UploadIBANRegistryResult(total_records=records_saved)

    """

    Find all records in the database
    """

    def find_all(self):

        return self.iban_registry_repository.find_all()
