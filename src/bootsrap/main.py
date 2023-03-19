import uvicorn
from fastapi import FastAPI

from src.application.customer_api import CustomerAPI
from src.service.customer_service import CustomerService
from src.service.customer_repository_service import CustomerRepositoryService


def build_application() -> FastAPI:
    in_memory_customer_repository_service = CustomerRepositoryService()
    customer_service = CustomerService(in_memory_customer_repository_service)
    return CustomerAPI(customer_service)


if __name__ == "__main__":
    uvicorn.run(app=build_application())
