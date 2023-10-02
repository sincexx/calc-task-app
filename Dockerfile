# Используем базовый образ Python 3.11
FROM python:3.11.5

# Устанавливаем переменную окружения для Python
ENV PYTHONUNBUFFERED 1

# Создаем директорию /app внутри контейнера
RUN mkdir /app

# Устанавливаем рабочую директорию /app
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории в контейнер
COPY . /app/

# Экспонируем порт 8000, который будет использоваться Uvicorn
EXPOSE 8000

# Запускаем Uvicorn для FastAPI приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]