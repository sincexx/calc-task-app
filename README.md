# Calculation Task App

## Деплой с помощью докера
1. docker build -t calc_task_app . 
2. docker run -p 8000:8000 calc_task_app

## Запуск тестов 
1. docker exec -it <id_запущенного_контейнера> /bin/bash
2. pytest --cov
## Документация
http://localhost:8000/redoc


## Версия Python
Python 3.11.5