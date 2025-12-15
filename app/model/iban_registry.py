from pydantic import BaseModel
from typing import Optional
from .iban_registry_element import IBANRegistryElement
from .iban_registry_bban import IBANRegistryBBAN
from .iban_registry_iban import IBANRegistryIBAN
from .iban_registry_contact_details import IBANRegistryContactDetails
from .iban_registry_updates import IBANRegistryUpdates
from .iban_registry_contact import IBANRegistryContact

class IBANRegistry(BaseModel):
    data_element: Optional[IBANRegistryElement] = None
    bban: Optional[IBANRegistryBBAN] = None
    iban: Optional[IBANRegistryIBAN] = None
    contact_details: Optional[IBANRegistryContactDetails] = None
    updates: Optional[IBANRegistryUpdates] = None
