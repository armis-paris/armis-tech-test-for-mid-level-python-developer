from typing import Protocol
import pandas as pd
from pydantic import BaseModel, validator

from src.contracts.customer_contract import CustomerRequest, CustomerResponse


class CustomerRepositoryProtocol(Protocol):
    def register_customer(self, customer: CustomerRequest):
        ...

    def fetch_number_of_customers(self) -> int:
        ...

    def get_customers(self) -> list[CustomerResponse]:
        ...


class CustomerService:
    def __init__(self, customer_repository_service: CustomerRepositoryProtocol):
        self.__customer_repository_service = customer_repository_service

    def register_customer(self, customer: CustomerRequest) -> None:
        self.__customer_repository_service.register_customer(customer=customer)

    def fetch_number_of_customers(self) -> int:
        return self.__customer_repository_service.fetch_number_of_customers()

    def get_customers(self) -> list[CustomerResponse]:
        return self.__customer_repository_service.get_customers()
