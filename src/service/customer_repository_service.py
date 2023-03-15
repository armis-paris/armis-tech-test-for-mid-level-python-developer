import pandas as pd


class CustomerRepositoryService:

    def __init__(self):
        self.__customer_list = pd.DataFrame({'name': ['kurt'],
                                             'surname': ['cobain'],
                                             'age': [27],
                                             'mail_domain': ['gmail.com']})

    def register_customer(self, customer: pd.DataFrame):
        self.__customer_list = pd.concat([self.__customer_list, customer])

    def fetch_number_of_customers(self) -> int:
        return len(self.__customer_list)
