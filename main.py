import logging
import uuid
from typing import Any

from fastapi import FastAPI, BackgroundTasks, HTTPException

from app.constants import TaskStatuses, TASK_NOT_FOUND_DETAIL, TASK_IN_PROGRESS_DETAIL
from app.schemas import BaseTaskModel, CreateTaskRequestModel, GetCalculationTaskResultModel, \
    ListTasksModelInfo
from app.task_manager import TaskManager
from app.tasks import perform_calculation_task

app = FastAPI(
    title='Calculation Task App',
    version='1.0.0',
    contact={'email': 'stakhanov.home@gmail.com'},
)

task_manager = TaskManager()

logging.basicConfig(filename='calc.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Метод для создания фоновой задачи
@app.post('/run_task/', response_model=BaseTaskModel)
async def run_task(
        background_tasks: BackgroundTasks,
        body: CreateTaskRequestModel
) -> Any:
    task = task_manager.create_task(
        x=body.x,
        y=body.y,
        operator=body.operator
    )
    background_tasks.add_task(perform_calculation_task, task)
    logger.info(f'Task {task.id} created')

    return {
        'id': task.id
    }


@app.get(
    '/get_result/{task_id}',
    response_model=GetCalculationTaskResultModel,
    response_model_exclude_none=True,
)
async def get_result(task_id: uuid.UUID) -> Any:
    task = task_manager.tasks.get(task_id)

    if not task:
        logger.warning(f'{TASK_NOT_FOUND_DETAIL}: {task_id}')
        raise HTTPException(status_code=404, detail=TASK_NOT_FOUND_DETAIL)
    if task.status == TaskStatuses.STARTED:
        logger.warning(f'{TASK_IN_PROGRESS_DETAIL}: {task_id}')
        logger.info(f'Task {task.id} created')
        raise HTTPException(status_code=400, detail=TASK_IN_PROGRESS_DETAIL)

    return {
        'description': task.description,
        'result': task.data.get('result')
    }


# Метод для получения списка асинхронных задач и их статусов
@app.get('/get_tasks_info/', response_model_exclude_none=True, response_model=ListTasksModelInfo)
async def get_tasks_info():
    logger.info(f'Tasks count: {len(task_manager.tasks.values())}')
    return {
        'info': [
            {
                'id': task.id,
                'status': task.status,
            } for task in task_manager.tasks.values()
        ]
    }
