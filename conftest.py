import requests
import pytest
from data_generators import register_new_courier_and_return_login_password
import urls

@pytest.fixture()
def response_login_pass():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass

    sign_in = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    courier_signin = requests.post(urls.MAIN_URL + urls.Hands.LOGIN, data=sign_in)
    courier_id = courier_signin.json()["id"]
    requests.delete(urls.MAIN_URL + urls.Hands.LOGIN + str(courier_id))