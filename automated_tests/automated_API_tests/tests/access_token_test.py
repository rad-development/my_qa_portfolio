# автотест для тест кейсов: TC_AUTH_001, TC_AUTH_002, TC_AUTH_003, TC_AUTH_004, TC_AUTH_005
import pytest
import requests
import random
import math
import time

# Генерация случайных координат
def random_lat():
    return round(random.uniform(-90, 90), 6)

def random_lon():
    return round(random.uniform(-180, 180), 6)

TITLE = "My favorite place"
COLOR = "RED"

FAVORITES_URL = "https://regions-test.2gis.com/v1/favorites"
AUTH_URL = "https://regions-test.2gis.com/v1/auth/tokens"

# Варианты токена для теста
token_cases = {
    "valid_token": True,             # получаем нормальный токен
    "no_token": None,                # не передаём токен
    "empty_token": "",               # передаём пустой токен
    "string_token": "not a token",   # значение строка
    "real_expired_token": "real"     # реально просроченный через 3 сек
}

@pytest.mark.parametrize("case, use_token", token_cases.items())
def test_favorites_token(case, use_token):
    lat = random_lat()
    lon = random_lon()
    data = {
        "title": TITLE,
        "lat": lat,
        "lon": lon,
        "color": COLOR
    }

    cookies = {}

    # Получаем нормальный токен, если требуется
    if use_token == True:
        auth_response = requests.post(AUTH_URL)
        token = auth_response.cookies.get("token")
        if not token:
            raise Exception("Не удалось получить сессионный токен")
        cookies = {"token": token}

    elif case == "real_expired_token":
        # Получаем нормальный токен
        auth_response = requests.post(AUTH_URL)
        token = auth_response.cookies.get("token")
        if not token:
            raise Exception("Не удалось получить сессионный токен")
        # Ждём 3 секунды, чтобы токен стал просроченным
        time.sleep(3)
        cookies = {"token": token}

    elif isinstance(use_token, str):
        cookies = {"token": use_token}  # пустой или string

    response = requests.post(FAVORITES_URL, data=data, cookies=cookies)

    # Определяем ожидаемый статус
    if case == "valid_token":
        expected_status = 200
    else:
        expected_status = 401  # все недействительные токены

    assert response.status_code == expected_status, f"{case}: expected {expected_status}, got {response.status_code}"

    # Проверка ответа только для валидного токена
    if expected_status == 200:
        json_data = response.json()
        assert "id" in json_data and isinstance(json_data["id"], int)
        assert json_data["title"] == TITLE
        assert json_data["color"] == COLOR
        assert math.isclose(json_data["lat"], lat, rel_tol=1e-6)
        assert math.isclose(json_data["lon"], lon, rel_tol=1e-6)
        assert "created_at" in json_data
