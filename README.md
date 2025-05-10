# 📚 Library Management System

Приложение для управления библиотекой: добавление книг, заимствование, возврат, просмотр истории, роли «читатель» и «библиотекарь».

---

## 🧪 Как запустить

### ✅ Установка зависимостей
```bash
pip install -r requirements.txt
```

### 🗃️ Настройка базы данных PostgreSQL
1. Создайте базу данных с именем `library`
2. В файле `server/database.py` замените параметры подключения (логин, пароль и хост).

### ⚒️ Миграции с Alembic
```bash
alembic init alembic
# настройте alembic.ini и alembic/env.py
alembic revision --autogenerate -m "Initial"
alembic upgrade head
```

---

## 🚀 Запуск приложения

### 🔧 Запуск сервера
```bash
cd server
python app.py
```

### 🖥️ Запуск клиента
```bash
cd client
python main.py
```

---

## ✅ Запуск тестов
```bash
pytest tests/test_logic.py
```