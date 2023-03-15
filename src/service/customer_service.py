import pandas as pd

from src.service.customer_repository_service import CustomerRepositoryService


class CustomerService:

    def register_customer(self, name: str, surname: str, age: int, mail_address: str) -> int:
        if name is None:
            raise Exception()
        if len(name) == 0:
            raise Exception()
        if surname is None:
            raise Exception()
        if len(surname) == 0:
            raise Exception()
        if age is None:
            raise Exception()
        if age < 12:
            raise Exception()
        name = name.lower()
        surname = name.lower()
        mail_domain = mail_address.split('@')[1]
        c = pd.DataFrame({'name': [name],
                          'surname': [surname],
                          'age': [age],
                          'mail_domain': [mail_domain]})
        s = CustomerRepositoryService()
        s.register_customer(c)
        return s.fetch_number_of_customers()
