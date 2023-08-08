DjangoCRUD
(M3-Core, ObjectPack)

Чтобы запустить проект, Вам потребуется:

- Клонировать репозиторий на свой ПК: https://github.com/tatarin10703/DjangoCRUD
- Установить зависимости из файла requirements.txt: pip install -r requirements.txt
- Создать и настройть базу БД: 

    python manage.py makemigrations
    
    python manage.py migrate
- Запустить сервер: 

    python manage.py runserver

Примечание:

Возможна ошибка (~ cannot import name 'Name' from 'collections') это связано с используемой версией Python (я использовал 3.10).  Во избежании ошибок требуется обратить внимание на исходные файлы библиотек и исправить from collections import ~  на from collections.abc import ~ .