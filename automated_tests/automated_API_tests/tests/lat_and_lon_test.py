# автотест для тест кейса: TC_FAV_001
import pytest
import requests
import json
import math
from pathlib import Path

# Путь к файлу JSON
test_data_file = Path(__file__).parent.parent / "test_data" / "test_data_lon_and_lat.json"

# Загружаем данные
with open(test_data_file, encoding="utf-8") as f:
    test_data = json.load(f)

lat_values = test_data["lat_values"]
lon_values = test_data["lon_values"]

# Генерируем пары значений
test_pairs = list(zip(lat_values, lon_values))

@pytest.mark.parametrize("lat, lon", test_pairs)
def test_create_favorite(lat, lon):
    # Получаем токен каждый раз
    auth_url = "https://regions-test.2gis.com/v1/auth/tokens"
    auth_response = requests.post(auth_url)
    token = auth_response.cookies.get("token")
    if not token:
        raise Exception("Не удалось получить сессионный токен")

    favorites_url = "https://regions-test.2gis.com/v1/favorites"
    data = {
        "title": "my fav place",
        "lat": lat,
        "lon": lon,
        "color": "RED"
    }

    response = requests.post(favorites_url, data=data, cookies={"token": token})

    # Проверяем валидность координат
    valid_coords = isinstance(lat, (int, float)) and isinstance(lon, (int, float)) and -90 <= lat <= 90 and -180 <= lon <= 180

    if valid_coords:
        # Проверка HTTP-кода
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # Проверка полей ответа
        json_data = response.json()
        assert "id" in json_data and isinstance(json_data["id"], int)
        assert json_data["title"] == data["title"]
        assert math.isclose(json_data["lat"], data["lat"], rel_tol=1e-6)
        assert math.isclose(json_data["lon"], data["lon"], rel_tol=1e-6)
        assert json_data["color"] == data["color"]
        assert "created_at" in json_data
    else:
        # Для некорректных координат сервер должен вернуть 400
        assert response.status_code == 400
