# Интернет-магазин на Django

Это простое веб-приложение интернет-магазина, реализованное с использованием **Django**, **Class-Based Views (CBV)** и **автоматизированных тестов через Pytest**.

## 🧩 Функционал

- Отображение списка товаров (`ListView`)
- Просмотр деталей товара (`DetailView`)
- Добавление новых товаров (`CreateView`)
- Редактирование товаров (`UpdateView`)
- Удаление товаров (`DeleteView`)
- Полностью покрыто автотестами через `pytest` и `pytest-django`

## 📦 Технологии

- Python 3.13
- Django 5.x
- HTML + шаблоны Django
- SQLite (по умолчанию)
- Poetry (управление зависимостями)
- pytest (для тестирования)

## 🚀 Установка и запуск

1. Клонируйте репозиторий (если в Git):
    ```bash
    git clone https://github.com/ вашеимя/online-shop.git
    cd online-shop
2. Активируйте виртуальное окружение:
   ```bash
   eval $(poetry env activate)
3. Установите зависимости:
    ```bash
    poetry install
4. Примените миграции:
    ```bash
    poetry run python manage.py migrate
5. Создайте суперпользователя:
    ```bash
    poetry run python manage.py createsuperuser
6. Запустите Redis:
- Убедитесь, что Redis установлен и доступен по адресу redis://127.0.0.1:6379/0.
   ```bash
   redis-server
7. Запустите Celery worker:
   ```bash
   poetry run celery -A config.celery.app worker --loglevel=info -P eventlet
## ⚠️ На Windows обязательно используйте -P eventlet или -P gevent, так как стандартный пул несовместим. 
8. Запустите сервер:
    ```bash
    poetry run python manage.py runserver
9. Откройте браузер и перейдите по ссылкам:
- Главная: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/
- Добавить товар: http://127.0.0.1:8000/product/new/
## При добавлении нового товара в консоль Celery будет выводиться сообщение:
- "Новый товар добавлен: Название_товара"
## 🧪 Запуск тестов
   ```bash
   poetry run pytest
   ```
## 📁 Структура проекта

- online-shop/
- ├── config/                  
- ├── products/                
- │   ├── models.py            
- │   ├── views.py             
- │   ├── urls.py              
- │   ├── forms.py             
- │   ├── tasks.py             
- │   └── tests/               
- ├── templates/               
- │   ├── base.html
- │   ├── product_list.html
- │   ├── product_detail.html
- │   ├── product_form.html
- │   └── product_confirm_delete.html
- ├── manage.py
- ├── pyproject.toml           
- └── README.md                