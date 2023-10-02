from enum import Enum


class TaskStatuses(Enum):
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"


class CalculationOperators(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"


ZERO_DIVISION_WARNING = "Zero division not allowed"

TASK_NOT_FOUND_DETAIL = "Task not found"
TASK_IN_PROGRESS_DETAIL = "Task is still in progress"
