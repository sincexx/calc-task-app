from typing import List
from uuid import UUID

from pydantic import BaseModel, field_validator

from app.constants import CalculationOperators


class BaseTaskModel(BaseModel):
    id: UUID


class CreateTaskRequestModel(BaseModel):
    x: int
    y: int
    operator: str

    @field_validator("operator")
    def validate_operator(cls, value):
        valid_operators = {o.value for o in CalculationOperators}
        if value not in valid_operators:
            raise ValueError(
                f"Invalid operator. Allowed operators are {valid_operators}"
            )
        return value


class GetCalculationTaskResultModel(BaseModel):
    description: str | None = None
    result: int | float | None = None


class TasksModelInfo(BaseTaskModel):
    status: str


class ListTasksModelInfo(BaseModel):
    info: List[TasksModelInfo]
