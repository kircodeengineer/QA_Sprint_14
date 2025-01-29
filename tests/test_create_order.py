import pytest
import requests
import urls
from data_generators import generate_random_order_payload

@pytest.mark.parametrize("color", [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    []
])
def test_create_order(color):
    payload = generate_random_order_payload(color)
    print(urls.main_url + urls.Hands.orders)
    response = requests.post(urls.main_url + urls.Hands.orders, json=payload)

    assert response.status_code == 201
    assert "track" in response.json()