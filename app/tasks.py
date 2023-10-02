from app.calculation import perform_calculation
from app.constants import TaskStatuses, ZERO_DIVISION_WARNING
from app.task_manager import Task


async def perform_calculation_task(task: Task) -> None:
    result = perform_calculation(
        x=task.data["x"], y=task.data["y"], operator=task.data["operator"]
    )

    if not result:
        task.status = TaskStatuses.FAILED.value
        task.data["result"] = None
        task.description = ZERO_DIVISION_WARNING
    else:
        task.status = TaskStatuses.COMPLETED.value
        task.data["result"] = result
