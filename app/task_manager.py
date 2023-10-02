from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Dict, Optional
from uuid import UUID, uuid4

from app.constants import TaskStatuses


@dataclass
class Task:
    data: dict
    description: str | None = None
    id: UUID = field(default_factory=uuid4)
    status: str = TaskStatuses.STARTED.value


class TaskManager:
    def __init__(self):
        self.tasks: Dict[UUID, Task] = {}

    def create_task(self, **data) -> Task:
        task = Task(data=data)
        self.tasks[task.id] = task
        return task
