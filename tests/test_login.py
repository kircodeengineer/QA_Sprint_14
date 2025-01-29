import requests
import urls

class TestLogin:
    def test_login_success(self, response_login_pass):
        login_pass = response_login_pass[1]

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(urls.main_url + urls.Hands.login, json=payload)

        assert response.status_code == 200
        assert "id" in response.json()