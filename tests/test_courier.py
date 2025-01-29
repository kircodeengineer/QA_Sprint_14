import pytest
import requests
import urls
from data_generators import generate_random_payload

class TestCourierCreate:
    def test_new_courier_success(self, response_login_pass):
        response = response_login_pass[0]
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    def test_same_courier_fail(self, response_login_pass):
        login_pass = response_login_pass[1]

        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }

        response = requests.post(urls.main_url + urls.Hands.courier, data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_with_missing_field_fail(self, missing_field):
        payload = generate_random_payload()

        payload.pop(missing_field)

        response = requests.post(urls.main_url + urls.Hands.courier, json=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

