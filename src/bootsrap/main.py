import uvicorn
from fastapi import FastAPI

from src.application.customer_api import CustomerAPI
from src.service.customer_service import CustomerService


def build_application() -> FastAPI:
    customer_service = CustomerService()
    return CustomerAPI(customer_service)


if __name__ == '__main__':
    uvicorn.run(app=build_application())
