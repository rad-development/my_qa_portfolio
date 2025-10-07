# автотест для тест кейса: TC_FAV_002
import pytest
import requests
import json
import math
import string
from pathlib import Path

# Загружаем данные из JSON
test_data_file = Path(__file__).parent.parent / "test_data" / "test_data_titles.json"
with open(test_data_file, encoding="utf-8") as f:
    test_data = json.load(f)

test_pairs = list(test_data.items())

LAT = 55.343454
LON = 67.434456

LATIN = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CYRILLIC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" \
           "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# Добавляем стандартные знаки препинания + пробел + среднее и длинное тире
ALLOWED_CHARS = LATIN + CYRILLIC + string.digits + string.punctuation + " –—"

def is_valid_title(title):
    if not isinstance(title, str):
        return False
    # Убираем пробелы по краям и проверяем длину
    stripped = title.strip()
    if not (1 <= len(stripped) <= 999):
        return False
    # Проверяем допустимые символы
    return all(c in ALLOWED_CHARS for c in title)


@pytest.mark.parametrize("desc, title", test_pairs)
def test_create_favorite_title(desc, title):
#    print(f"Testing title ({desc}): {title}")  # Здесь видно любые символы
    # Получаем токен
    auth_url = "https://regions-test.2gis.com/v1/auth/tokens"
    auth_response = requests.post(auth_url)
    token = auth_response.cookies.get("token")
    if not token:
        raise Exception("Не удалось получить сессионный токен")

    favorites_url = "https://regions-test.2gis.com/v1/favorites"
    data = {
        "title": title,
        "lat": LAT,
        "lon": LON
    }

    response = requests.post(favorites_url, data=data, cookies={"token": token})

    if is_valid_title(title):
        assert response.status_code == 200, f"Expected 200, got {response.status_code} for {desc}"
        json_data = response.json()
        assert "id" in json_data and isinstance(json_data["id"], int)
        assert json_data["title"] == data["title"]
        assert math.isclose(json_data["lat"], data["lat"], rel_tol=1e-6)
        assert math.isclose(json_data["lon"], data["lon"], rel_tol=1e-6)
        assert "created_at" in json_data
    else:
        assert response.status_code == 400, f"Expected 400, got {response.status_code} for {desc}"
