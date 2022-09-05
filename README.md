# Сайт с подборкой интересных мест

Сайт повзоляет отмечать на карте инетерсные с места с описанием и фотограифями

## Установка

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Создайте файл с переменными окружения.


### Переменные окружения .env

Создайте файл ``.env`` в корневой папке следующего вида:

```
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=
DATABASE_URL=
```

- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта, его можно получуить следуюющим образом:

```
python .\manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```

- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_URL` — адрес к базе данных, например: `sqlite:///db.sqlite3`. 
- Больше информации в [документации](https://github.com/jacobian/dj-database-url#url-schema)
. Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.

### Запуск

Запустите сервер командой `python3 manage.py runserver`  

## Загрузка данных
Реализована возможность загрузки данных с помощью json файла:
```
python manage.py load_place -j place.json
```
`place.json` - любой локальный или сетевой файл вида:
```
["places":{
	"title": string,
	"imgs": [
		link,
	],
	"description_short": text
	"description_long": html,
	"coordinates": {
		"lng": float,
		"lat": float
	}
}]
```
### Загрузка демо данных

Загрузите демо-данные командой:

```
python manage.py load_place -j demo.json
```

## Пример реализации
[pythonanywhere](https://axrasp.pythonanywhere.com/)