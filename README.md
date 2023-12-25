# Сервер по размещению объявлений

## Стек:
- Python 3.10
- FastAPI 0.105.0
- SQLAlchemy 2.0.23
- PostgreSQL 15.4

## Запуск проекта:
1. Установите и активируйте виртуальное окружение:  
Введите в терминале  
`python3 -m venv venv`  
`venv\Scripts\activate`  


2. Установите зависимости:  
Введите в терминале `pip install -r requirements.txt`


3. Конфигурация:  
Создайте файл .env в папке с проектом и укажите в нём:  
   - Хост PostgreSQL. Пример: DB_HOST=localhost
   - Порт PostgrSQL. Пример: DB_PORT=5432
   - Название базы данных. Пример: DB_NAME=SurfIT
   - Имя пользователя в PostgreSQL: Пример: DB_USER=postgres
   - Пароль этого пользователя в PostgreSQL. Пример: DB_PASS=postgres
   - Ключ для шифрования JWT тоекна. Пример: SECRET_KEY=secret-key
  

4. Примените миграции:  
Введите в терминале `alembic upgrade head`


6. Запуск:  
Введите в терминале `uvicorn app.main:app --reload`  
Проект запустится по адресу http://127.0.0.1:8000/docs#/
