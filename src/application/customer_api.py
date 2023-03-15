from fastapi import FastAPI

from src.service.customer_service import CustomerService


class CustomerAPI(FastAPI):
    __customer_service: CustomerService

    def __init__(self, customer_service: CustomerService):
        self.__customer_service = customer_service

        super().__init__()

        @self.get('/customer-service/api/v1/register-customer')
        def register_customer(name: str, surname: str, age: int, mail_address: str):
            number_of_customers =  self.__customer_service.register_customer(surname, name, age, mail_address)
            return {'number_of_customers': number_of_customers}
