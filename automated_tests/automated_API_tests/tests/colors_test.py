# автотест для тест кейса: TC_FAV_003
import pytest
import requests
import json
import random
from pathlib import Path

# Генерация случайных координат
def random_lat():
    return round(random.uniform(-90, 90), 6)

def random_lon():
    return round(random.uniform(-180, 180), 6)

# Загружаем данные из JSON
test_data_file = Path(__file__).parent.parent / "test_data" / "test_data_colors.json"
with open(test_data_file, encoding="utf-8") as f:
    test_data = json.load(f)

test_pairs = list(test_data.items())

ALLOWED_VALUES = {"BLUE", "GREEN", "RED", "YELLOW", None}

TITLE = "My favorite place"

@pytest.mark.parametrize("desc, color", test_pairs)
def test_create_favorite_color(desc, color):
    lat = random_lat()
    lon = random_lon()

    # Получаем токен
    auth_url = "https://regions-test.2gis.com/v1/auth/tokens"
    auth_response = requests.post(auth_url)
    token = auth_response.cookies.get("token")
    if not token:
        raise Exception("Не удалось получить сессионный токен")

    favorites_url = "https://regions-test.2gis.com/v1/favorites"
    data = {
        "title": TITLE,
        "lat": lat,
        "lon": lon,
        "color": color
    }

    response = requests.post(favorites_url, data=data, cookies={"token": token})

    # Определяем ожидаемый статус
    expected_status = 200 if color in ALLOWED_VALUES else 400
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code} for {desc}"

    if expected_status == 200:
        json_data = response.json()
        assert "id" in json_data and isinstance(json_data["id"], int)
        assert json_data["title"] == TITLE
        assert json_data["color"] == color
        assert round(json_data["lat"], 6) == lat
        assert round(json_data["lon"], 6) == lon
        assert "created_at" in json_data
