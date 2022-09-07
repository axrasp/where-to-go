# Сайт с подборкой интересных мест

Сайт повзоляет отмечать на карте инетерсные с места с описанием и фотограифями

## Установка

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл с переменными окружения.
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`

### Переменные окружения .env

Создайте файл ``.env`` в корневой папке следующего вида (пример файла ``example.env``):

```
DEBUG='False'
SECRET_KEY='aywt$0b_i415ppej$-2(g26&+d-0nAx+r*vb(sclv2#0tpfnhmq'
STATIC_ROOT='assets'
ALLOWED_HOSTS=''
DATABASE_URL='sqlite:///db.sqlite3'
```

- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта, его можно получуить следуюющим образом:

```
python manage.py shell
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
python manage.py load_place -p your_json_path  #в случае локального файла
python manage.py load_place -u http://your-url.com  #в случае сетевого расположения файла (URL)
```

Файл JSON должен иметь вид:

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