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

### 🎯 Ключевые возможности

- **🔐 JWT-аутентификация** — Безопасная регистрация и вход пользователей с использованием JWT-токенов
- **💬 Интеграция с LLM** — Бесшовное подключение к 100+ языковым моделям через OpenRouter
- **📝 История диалогов** — Постоянное хранение истории общения в SQLite
- **🏗️ Чистая архитектура** — Разделение на слои API, бизнес-логики, репозиториев и сервисов
- **⚡ Асинхронная производительность** — Полностью асинхронные операции для высокой конкурентности
- **📚 Автодокументация** — Интерактивные Swagger UI и ReDoc из коробки
- **🐍 Современный Python** — Типизация, Pydantic v2 и асинхронный SQLAlchemy
- **📦 Быстрое управление пакетами** — Использование `uv` для молниеносной установки зависимостей

---

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
