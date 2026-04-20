# 🤖 LLM-P: Защищённое API для работы с большими языковыми моделями

<div align="center">

[![FastAPI](https://img.shields.io/badge/FastAPI-0.112+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-FF6B6B?style=for-the-badge&logo=openai&logoColor=white)](https://openrouter.ai/)
[![uv](https://img.shields.io/badge/uv-Быстрый%20менеджер%20пакетов-6E4B8B?style=for-the-badge)](https://github.com/astral-sh/uv)

**Защищённый API-сервис для взаимодействия с большими языковыми моделями через OpenRouter**

[Возможности](#-возможности) • [Быстрый старт](#-быстрый-старт) • [Документация API](#-документация-api) • [Архитектура](#-архитектура) • [Разработка](#-разработка)

</div>

---

## 📋 Обзор проекта

LLM-P — это готовый к использованию сервис на FastAPI, предоставляющий защищённый интерфейс для взаимодействия с большими языковыми моделями через сервис OpenRouter. Приложение реализует JWT-аутентификацию, постоянное хранение истории диалогов и следует принципам чистой архитектуры с чётким разделением ответственности.



## 🚀 Быстрый старт

### Предварительные требования

- Python 3.11 или выше
- Менеджер пакетов [uv](https://github.com/astral-sh/uv)
- API-ключ OpenRouter ([получить здесь](https://openrouter.ai/keys))

### Установка

```bash
# 1. Клонирование репозитория
git clone https://github.com/yourusername/llm-p.git
cd llm-p

# 2. Установка uv
pip install uv

# 3. Создание виртуального окружения и установка зависимостей
uv venv
source .venv/bin/activate  # На Windows: .venv\Scripts\activate.bat
uv pip install -e .

# 4. Настройка переменных окружения
cp .env.example .env
# Отредактируйте .env и добавьте ваш API-ключ OpenRouter

# 5. Запуск сервера
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
---

---

## 📸 Скриншоты работы приложения

### 1. Запуск сервера и проверка кода

| Запуск Uvicorn | Проверка Ruff |
|:---:|:---:|
| ![Запуск сервера](./s/Вставленное%20изображение.png) | ![Ruff check](./s/Снимок%20экрана%20от%202026-04-20%2020-33-31.png) |

*Успешный запуск сервера на http://0.0.0.0:8000 и проверка кода линтером ruff*

---

### 2. Swagger UI — Документация API

![Swagger UI](./s/Вставленное%20изображение%20(2).png)

*Главная страница интерактивной документации Swagger со всеми доступными эндпоинтами*

---

### 3. Аутентификация

| Регистрация | Логин | Профиль |
|:---:|:---:|:---:|
| ![Регистрация](./s/Вставленное%20изображение%20(3).png) | ![Логин](./s/Вставленное%20изображение%20(4).png) | ![Профиль](./s/Вставленное%20изображение%20(5).png) |

- **Регистрация** (`POST /auth/register`) — Создание нового пользователя
- **Логин** (`POST /auth/login`) — OAuth2 форма для получения JWT токена
- **Профиль** (`GET /auth/me`) — Получение данных текущего пользователя

---

### 4. Работа с чатом и LLM

| Запрос к LLM | История чата |
|:---:|:---:|
| ![Чат запрос](./s/Вставленное%20изображение%20(6).png) | ![История](./s/Вставленное%20изображение%20(7).png) |

- **Чат** (`POST /chat`) — Отправка промпта и получение ответа от OpenRouter
- **История** (`GET /chat/history`) — Просмотр сохранённой истории диалога

---

### 5. Проверка работоспособности

![Health Check](./s/Вставленное%20изображение%20(8).png)

*Эндпоинт `/health` возвращает статус сервера и текущее окружение*



