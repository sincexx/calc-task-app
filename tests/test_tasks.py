import pytest

from app.constants import TaskStatuses, ZERO_DIVISION_WARNING
from app.task_manager import Task
from app.tasks import perform_calculation_task


@pytest.mark.asyncio
async def test_perform_calculation_task_completed():
    # Создаем задачу с допустимыми данными
    task_data = {"x": 6, "y": 3, "operator": "+"}
    task = Task(data=task_data)

    # Запускаем функцию perform_calculation_task
    await perform_calculation_task(task)

    # Проверяем, что статус задачи стал COMPLETED
    assert task.status == TaskStatuses.COMPLETED.value

    # Проверяем, что результат вычисления добавлен в данные задачи
    assert "result" in task.data


@pytest.mark.asyncio
async def test_perform_calculation_task_failed_zero_division():
    # Создаем задачу с делением на ноль
    task_data = {"x": 5, "y": 0, "operator": "/"}
    task = Task(data=task_data)

    # Запускаем функцию perform_calculation_task
    await perform_calculation_task(task)

    # Проверяем, что статус задачи стал FAILED
    assert task.status == TaskStatuses.FAILED.value

    # Проверяем, что результат установлен как None
    assert task.data["result"] is None

    # Проверяем, что описание задачи установлено как ZERO_DIVISION_WARNING
    assert task.description == ZERO_DIVISION_WARNING
