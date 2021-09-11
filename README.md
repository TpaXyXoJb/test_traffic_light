README
=====================

Этот README документирует описывает все шаги, необходимые для запуска веб-приложения.

### Создать и применить миграции

* `python manage.py makemigrations`
* `python manage.py migrate`

### Получить необходимые данные JSON

* `python parse_data.py`

### Загрузить фикстуры в базу данных

* `python manage.py loaddata users_data.json posts_data.json`

### Запустить локальный веб-сервер 

* `python manage.py runserver`

### Перейти по адресу

* http://localhost:8000

