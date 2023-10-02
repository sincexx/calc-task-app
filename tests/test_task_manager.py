import pytest
from app.task_manager import TaskManager
from app.constants import TaskStatuses


@pytest.fixture
def task_manager():
    return TaskManager()


def test_create_task(task_manager):
    data = {"key": "value"}
    task = task_manager.create_task(**data)

    assert task.data == data
    assert task.description is None
    assert task.status == TaskStatuses.STARTED.value


def test_task_manager(task_manager):
    data1 = {"key1": "value1"}
    data2 = {"key2": "value2"}

    task1 = task_manager.create_task(**data1)
    task2 = task_manager.create_task(**data2)

    assert len(task_manager.tasks) == 2
    assert task1.id in task_manager.tasks
    assert task2.id in task_manager.tasks
    assert task_manager.tasks[task1.id] == task1
    assert task_manager.tasks[task2.id] == task2
