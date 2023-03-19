import pandas as pd

from src.contracts.customer_contract import CustomerRequest, CustomerResponse


class CustomerRepositoryService:
    def __init__(self):
        self.__customer_list = pd.DataFrame(
            {
                "name": ["kurt"],
                "surname": ["cobain"],
                "age": [27],
                "mail_domain": ["gmail.com"],
            }
        )

    def register_customer(self, customer: CustomerRequest):
        self.__customer_list = pd.concat(
            [
                self.__customer_list,
                pd.DataFrame.from_records(
                    [
                        {
                            "name": customer.name,
                            "surname": customer.surname,
                            "age": customer.age,
                            "mail_domain": customer.mail_domain,
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )

    def fetch_number_of_customers(self) -> int:
        return len(self.__customer_list)

    def get_customers(self) -> list[CustomerResponse]:
        return [
            CustomerResponse.parse_obj(obj)
            for obj in self.__customer_list.to_dict(orient="records")
        ]
