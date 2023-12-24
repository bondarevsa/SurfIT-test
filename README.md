# Сервер по размещению объявлений

## Стек: 
- Python 3.10
- FastAPI
- SQLAlchemy
- PostgreSQL

## Запуск проекта:
1. Установите зависимости:  
Введите в терминале `pip install -r requirements.txt`  
2. Конфигурация:  
Создайте файл .env в папке с проектом и укажите в нём:
   - Хост PostgreSQL. Пример: DB_HOST=localhost
   - Порт PostgrSQL. Пример: DB_PORT=5432
   - Название базы данных. Пример: DB_NAME=SurfIT
   - Имя пользователя в PostgreSQL: Пример: DB_USER=postgres
   - Пароль этого пользователя в PostgreSQL. Пример: DB_PASS=postgres
   - Ключ для шифрования JWT тоекна. Пример: SECRET_KEY=secret-key
3. Запуск:  
Введите в терминале `uvicorn main:app --reload`
Проект запусится по адресу http://127.0.0.1:8000/docs#/ 
