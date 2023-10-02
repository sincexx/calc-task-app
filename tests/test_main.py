import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def test_client():
    return TestClient(app)


def test_run_calculation_task(test_client):
    # Отправляем POST-запрос к эндпоинту
    data = {"x": 5, "y": 3, "operator": "+"}
    response = test_client.post("/run_task/", json=data)

    # Проверяем статус-код ответа
    assert response.status_code == 200

    # Проверяем, что ответ содержит правильный ID задачи
    response_data = response.json()
    assert "id" in response_data


def test_get_calculation_task_result_task_not_found(test_client):
    # Отправляем GET-запрос с несуществующим task_id
    response = test_client.get(
        "/get_result/bd113d2b-3242-4c98-ae33-c0dcac1a6614"
    )

    # Проверяем, что статус-код ответа равен 404
    assert response.status_code == 404


def test_get_calculation_task_result_success(test_client):
    # Отправляем POST-запрос к эндпоинту
    data = {"x": 6, "y": 3, "operator": "+"}
    response = test_client.post("/run_task/", json=data)
    # Проверяем статус-код ответа
    assert response.status_code == 200

    # Проверяем, что ответ содержит правильный ID задачи
    response_data = response.json()
    assert "id" in response_data

    task_id = response_data["id"]
    # Отправляем GET-запрос с task_id задачи
    response = test_client.get(f"/get_result/{task_id}")

    # Проверяем, что статус-код ответа равен 200
    assert response.status_code == 200

    # Проверяем, что ответ содержит описание и результат
    response_data = response.json()
    assert "result" in response_data
