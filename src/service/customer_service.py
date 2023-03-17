import pandas as pd

from src.service.customer_repository_service import CustomerRepositoryService


class CustomerService:

    def register_customer(self, name: str, surname: str, age: int, mail_address: str) -> int:
        if not name:
            raise ValueError("Name is required")
        if not surname:
            raise ValueError("Surname is required")
        if age is None:
            raise ValueError("Age is required")
        if age < 12:
            raise ValueError("Customer must be at least 12 years old")

        name = name.lower()
        surname = surname.lower()
        mail_domain = mail_address.split('@')[1]
        customer = pd.DataFrame({'name': [name],
                                 'surname': [surname],
                                 'age': [age],
                                 'mail_domain': [mail_domain]})
        self._register_customer(customer)
        return self._fetch_number_of_customer()

    def _register_customer(self, customer: pd.DataFrame) -> None:
        repository = CustomerRepositoryService()
        repository.register_customer(customer)

    def _fetch_number_of_customer(self) -> int:
        repository = CustomerRepositoryService()
        return repository.fetch_number_of_customers()
