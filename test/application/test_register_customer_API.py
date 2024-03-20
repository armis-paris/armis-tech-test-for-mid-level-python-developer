from fastapi.testclient import TestClient
from src.application.customer_api import CustomerAPI
from src.service.customer_repository_service import CustomerRepositoryService
from src.service.customer_service import CustomerService


def setUpClient():
    in_memory_customer_repository_service = CustomerRepositoryService()
    print(in_memory_customer_repository_service.get_customers())
    customer_service = CustomerService(in_memory_customer_repository_service)
    return TestClient(CustomerAPI(customer_service))


def test_register_customer():
    client = setUpClient()
    response = client.get(
        "/customer-service/api/v1/register-customer?name=yamen1&surname=refaat1&age=30&mail_address=yamen_gamaleldin%40live.com"
    )
    assert response.status_code == 200
    assert response.json() == {"number_of_customers": 2}


def test_register_customer_v2():
    client = setUpClient()
    response = client.post(
        "/customer-service/api/v2/register-customer",
        json={
            "name": "yamen",
            "surname": "refaat",
            "age": 30,
            "mail_address": "yamen_gamaleldin@live.com",
        },
    )
    assert response.status_code == 201


def test_get_customers():
    client = setUpClient()
    client.post(
        "/customer-service/api/v2/register-customer",
        json={
            "name": "yamen",
            "surname": "refaat",
            "age": 30,
            "mail_address": "yamen_gamaleldin@live.com",
        },
    )
    response = client.get("/customer-service/api/v2/customers")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "kurt",
            "surname": "cobain",
            "age": 27,
            "mail_domain": "gmail.com",
        },
        {
            "name": "yamen",
            "surname": "refaat",
            "age": 30,
            "mail_domain": "live.com",
        },
    ]
