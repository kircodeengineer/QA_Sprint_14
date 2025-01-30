import allure
import pytest
import requests
import urls
from data_generators import generate_random_order_payload
from data import StatusCodes

class TestCreateOrder:
    @allure.title('Проверка Создания заказа c цветом самоката {color}')  # декораторы
    @allure.description('Проверка, что, когда создаёшь заказ:\n'
                            '- можно указать один из цветов — BLACK или GREY;\n'
                            '- можно указать оба цвета;\n'
                            '- можно совсем не указывать цвет;\n'
                            '- тело ответа содержит track.')
    @allure.testcase('ссылка на тест-кейс',                 'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_success(self, color):
        payload = generate_random_order_payload(color)
        response = requests.post(urls.MAIN_URL + urls.Hands.ORDERS, json=payload)
        assert response.status_code == StatusCodes.CODE_201
        assert "track" in response.json()