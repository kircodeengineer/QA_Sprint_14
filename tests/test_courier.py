import allure
import pytest
import requests
import urls
from data_generators import generate_random_payload
from data import StatusCodes, Messages

class TestCourierCreate:
    @allure.title('Проверка успешного Создания курьера')  # декораторы
    @allure.description('Проверка, что:\n'
                        '- курьера можно создать;\n'
                        '- чтобы создать курьера, нужно передать в ручку все обязательные поля;\n'
                        '- запрос возвращает правильный код ответа;\n'
                        '- запрос возвращает {"ok":true}.')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
    def test_new_courier_success(self, response_login_pass):
        response = response_login_pass[0]
        assert response.status_code == StatusCodes.CODE_201
        assert response.json() == {'ok': True}

    @allure.title('Проверка невозможности Создания курьера при вводе существующих регистрационных данных')  # декораторы
    @allure.description('Проверка, что курьер не создан и возвращается ошибка')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
    def test_same_courier_fail(self, response_login_pass):
        login_pass = response_login_pass[1]

        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }

        response = requests.post(urls.MAIN_URL + urls.Hands.COURIER, data=payload)

        assert response.status_code == StatusCodes.CODE_409
        assert response.json()["message"] == Messages.LOGIN_IS_USED

    @allure.title('Проверка невозможности Создания курьера, если отсутствует одно из полей регистрационных данных')  # декораторы
    @allure.description('Проверка, что курьер не создан и возвращается ошибка')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_with_missing_field_fail(self, missing_field):
        payload = generate_random_payload()

        payload.pop(missing_field)

        response = requests.post(urls.MAIN_URL + urls.Hands.COURIER, json=payload)

        assert response.status_code == StatusCodes.CODE_400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_TO_CREATE

