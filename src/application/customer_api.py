from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from src.contracts.customer_contract import CustomerResponse, CustomerRequest

from src.service.customer_service import CustomerService


class CustomerAPI(FastAPI):
    __customer_service: CustomerService

    def __init__(self, customer_service: CustomerService):
        self.__customer_service = customer_service

        super().__init__()

        # I think this should be a post request
        # Body should be an object using pydantic to validate the input
        # There must be validations on the input
        # The return value should have the correct status code
        @self.get("/customer-service/api/v1/register-customer")
        def register_customer_and_get_number_of_customers(
            name: str, surname: str, age: int, mail_address: str
        ):
            try:
                customer = CustomerRequest(
                    name=name, surname=surname, age=age, mail_address=mail_address
                )

            except ValidationError as e:
                return {"error": e.errors()}
            self.__customer_service.register_customer(customer)
            number_of_customers = self.__customer_service.fetch_number_of_customers()
            return {"number_of_customers": number_of_customers}

        @self.post("/customer-service/api/v2/register-customer")
        def register_customer(customer: CustomerRequest):
            self.__customer_service.register_customer(customer)
            return JSONResponse(jsonable_encoder(customer), status_code=201)

        @self.get("/customer-service/api/v2/customers")
        def get_customers() -> list[CustomerResponse]:
            return self.__customer_service.get_customers()
