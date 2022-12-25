import pytest
import requests
import allure
from selenium import webdriver


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'POST request to: {url}'):
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'GET request to: {url}'):
            return requests.get(url=url, params=params, headers=headers)


@pytest.fixture
def users_api():
    return ApiClient(base_address="https://jsonplaceholder.typicode.com/")


@pytest.fixture(scope="session")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(r'C:/Drivers/chromedriver.exe')
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("http://google.com/")
    driver.maximize_window()

    yield driver
    driver.close()