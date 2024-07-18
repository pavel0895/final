import allure
import pytest
from api_req import get_current_user
from config import API_KEY

@pytest.mark.parametrize("token, expected_status", [
    (API_KEY, 200),
    ("invalid_token", 401),
])
@allure.title("Получение текущего пользователя")
def test_get_current_user(token, expected_status):
    response = get_current_user(token)
    assert response.status_code == expected_status