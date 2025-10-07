# автотест для тест кейса: TC_FAV_004
import pytest
import requests
import random

# Генерация случайных координат
def random_lat():
    return round(random.uniform(-90, 90), 6)

def random_lon():
    return round(random.uniform(-180, 180), 6)

TITLE = "My favorite place"
COLOR = "GREEN"

# Кейсы: 1 = поле отправляем, 0 = не отправляем
cases = [
    (1, 0, 0, 0),
    (0, 0, 1, 1),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (1, 1, 0, 1),
    (1, 1, 1, 0),
    (1, 0, 1, 1),
    (1, 1, 1, 1),
]

@pytest.mark.parametrize("send_color, send_lat, send_lon, send_title", cases)
def test_favorite_required_fields(send_color, send_lat, send_lon, send_title):
    lat = random_lat()
    lon = random_lon()

    # Получаем токен
    auth_url = "https://regions-test.2gis.com/v1/auth/tokens"
    auth_response = requests.post(auth_url)
    token = auth_response.cookies.get("token")
    if not token:
        raise Exception("Не удалось получить сессионный токен")

    favorites_url = "https://regions-test.2gis.com/v1/favorites"

    # Формируем data только с нужными полями
    data = {}
    if send_color:
        data["color"] = COLOR
    if send_lat:
        data["lat"] = lat
    if send_lon:
        data["lon"] = lon
    if send_title:
        data["title"] = TITLE

    response = requests.post(favorites_url, data=data, cookies={"token": token})

    # Проверяем, отправлены ли все обязательные поля
    if send_lat and send_lon and send_title:
        expected_status = 200
    else:
        expected_status = 400

    assert response.status_code == expected_status, f"Case {send_color, send_lat, send_lon, send_title}: expected {expected_status}, got {response.status_code}"

    if expected_status == 200:
        json_data = response.json()
        assert "id" in json_data and isinstance(json_data["id"], int)
        assert json_data["title"] == TITLE
        if send_color:
            assert json_data["color"] == COLOR
        else:
            assert "color" in json_data  # цвет может быть пустым или None
        assert round(json_data["lat"], 6) == lat
        assert round(json_data["lon"], 6) == lon
        assert "created_at" in json_data
