# 📁 Design_studio

## 📖 Кратко о проекте

Учебный проект дизайн студии на Django. Помимо уже знакомых мне технологий,
мною впервые был опробован Pytest. 

---

## 🧾 TODO список (основные положения)

- [x] Инициировать проект (окружение, настройки, тестовый вывод стр. и др.).
- [x] Написанить полный CRUD для представлений. 
- [x] Наличие разных сущностей, начиная с отзыва, заканчивая услугами.
- [x] Научиться писать тесты на pytest. 
- [x] Запустить проект с помощью docker-compose файла, добавить балансировку 
нагрузок (nginx).

---

## 💻 Запуск проекта

0. Загрузка проекта и переход в директорию 

```bash
git clone git@github.com:SamvelMhitaryan/design_studio.git
```

1. Создание виртуального окружения (venv): 

```bash
python3 -m venv venv
```

2. Активация виртуального окружения (venv): 

Linux / Mac
```bash
. venv/bin/activate
```

Windows
```bash
. venv\scripts\activate
```

3. Установка зависимостей: 

```bash
pip install -r requirements.txt
```

4. Запуск: 

```bash
python3 manage.py runserver
```

# замена настроек БД и ключа django под себя.

python3 manage.py collectstatic    # \
python3 manage.py makemigrations   #  Или все одной командой через &&
python3 manage.py migrate          # /

python3 manage.py runserver 8000   # либо полноценно через gunicorn, nginx и т.д.
```