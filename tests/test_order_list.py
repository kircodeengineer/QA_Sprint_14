import allure
import requests
import urls

@allure.title('Проверка Списка заказов')  # декораторы
@allure.description('Проверка, что в тело ответа возвращается список заказов.')
@allure.testcase('ссылка на тест-кейс',                 'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/6831ee89-fac7-4a2b-8391-ce78603174df/sprints/371250/topics/b3967e08-29fd-4dc9-b4f2-e72d971421ec/lessons/3ff09270-409f-4302-a04a-c2f0297e9f69/')
def test_get_orders_list_returns_orders_list():
    response = requests.get(urls.main_url + urls.Hands.orders)
    assert response.status_code == 200
    assert "orders" in response.json()
    assert isinstance(response.json()["orders"], list)