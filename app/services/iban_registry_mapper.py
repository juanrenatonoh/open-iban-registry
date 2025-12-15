from typing import List

from ..model.iban_registry import (
    IBANRegistry,
    IBANRegistryElement,
    IBANRegistryBBAN,
    IBANRegistryIBAN,
    IBANRegistryContactDetails,
    IBANRegistryUpdates,
    IBANRegistryContact,
)


class IBANRegistryMapper:

    def __init__(self):
        pass

    """
    Map the description pattern example to the iban registry entity
    """

    def map_dict_to_iban_registry_list(self, data: dict) -> List[IBANRegistry]:

        registry_list = []

        for clave, values in data.items():

            if clave == "Data element":
                continue

            registry = IBANRegistry(
                data_element=IBANRegistryElement(
                    name_of_country=values[0],
                    iban_prefix_country_code_iso=values[1],
                    country_code_includes_other_countries_territories=values[2],
                    sepa_country=values[3],
                    sepa_country_also_includes=values[4],
                    domestic_account_number_example=values[5],
                ),
                bban=IBANRegistryBBAN(
                    bban=values[6],
                    bban_structure=values[7],
                    bban_length=values[8],
                    bank_identifier_position_within_the_bban=values[9],
                    bank_identifier_pattern=values[10],
                    branch_identifier_position_within_the_bban=values[11],
                    branch_identifier_pattern=values[12],
                    bank_identifier_example=values[13],
                    branch_identifier_example=values[14],
                    bban_example=values[15],
                ),
                iban=IBANRegistryIBAN(
                    iban=values[16],
                    iban_structure=values[17],
                    iban_length=values[18],
                    effective_date=values[19],
                    iban_electronic_format_example=values[20],
                    iban_print_format_example=values[21],
                ),
                contact_details=IBANRegistryContactDetails(
                    organisation=values[23],
                    department=values[24],
                    street_address=values[25],
                    city_postcode=values[26],
                    department_generic_email=values[27],
                    department_tel=values[28],
                    contacts=[
                        IBANRegistryContact(
                            priority="primary",
                            name=values[30],
                            first_name=values[31],
                            title=values[32],
                            email=values[33],
                            tel=values[34],
                        ),
                        IBANRegistryContact(
                            priority="secondary",
                            name=values[36],
                            first_name=values[37],
                            title=values[38],
                            email=values[39],
                            tel=values[40],
                        ),
                    ],
                ),
                updates=IBANRegistryUpdates(last_update_date=values[42]),
            )

            registry_list.append(registry)

        return registry_list
