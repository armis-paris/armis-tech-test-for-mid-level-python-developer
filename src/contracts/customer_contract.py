from pydantic import BaseModel, validator


class CustomerRequest(BaseModel):
    name: str
    surname: str
    age: int
    mail_address: str

    @validator("name")
    def name_must_not_be_empty(cls, v):
        if len(v) == 0:
            raise ValueError("name must not be empty")
        return v

    @validator("surname")
    def surname_must_not_be_empty(cls, v):
        if len(v) == 0:
            raise ValueError("surname must not be empty")
        return v

    @validator("age")
    def age_must_be_greater_than_12(cls, v):
        if v < 12:
            raise ValueError("age must be greater than 12")
        return v

    @validator("name", "surname")
    def name_and_surname_must_be_lowercase(cls, v):
        return v.lower()

    @validator("mail_address")
    def mail_address_must_be_valid(cls, v):
        if "@" not in v:
            raise ValueError("mail address must be valid")

        if len(v.split("@")[1]) == 0:
            raise ValueError("mail domain must be valid")

        return v

    @property
    def mail_domain(self):
        return self.mail_address.split("@")[1]


class CustomerResponse(BaseModel):
    name: str
    surname: str
    age: int
    mail_domain: str
