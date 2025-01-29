import allure
import pytest
import requests
import urls

class TestLoginCourier:
    @allure.title('Проверка успешной Авторизации курьера')  # декораторы
    @allure.description('Проверка, что:\n'
                        '- курьер может авторизоваться;\n'
                        '- успешный запрос возвращает id')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
    def test_login_success(self, response_login_pass):
        login_pass = response_login_pass[1]

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(urls.main_url + urls.Hands.login, json=payload)

        assert response.status_code == 200
        assert "id" in response.json()


    @allure.title('Проверка невозможности Авторизоваться если передать не все обязательные поля')  # декораторы
    @allure.description('Проверка, что если какого-то поля нет, запрос возвращает ошибку')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_failed_by_missing_field(self, response_login_pass, missing_field):
        login_pass = response_login_pass[1]
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        payload.pop(missing_field)

        response = requests.post(urls.main_url + urls.Hands.login, json=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка невозможности Авторизоваться под несуществующим пользователем')  # декораторы
    @allure.description('Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
    @pytest.mark.parametrize("wrong_data", ["login", "password"])
    def test_login_failed_by_wrong_data(self, response_login_pass, wrong_data):
        login_pass = response_login_pass[1]

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        payload[wrong_data] = "wrong_data"

        response = requests.post(urls.main_url + urls.Hands.login, json=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
