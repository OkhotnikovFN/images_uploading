# images_uploading-
Загрузка изображений в базу с компьютера или из интернета

* Приложение предназначено для загрузки изображений в базу с компютера или из сети интернет.
В качестве базы данных используется SQLite

* Шаги по установке, сборке, запуску:  
  1. Клонировать репозиторий на свою рабочую станцию
  2. Перейти в папку проекта и выполнить команды
  
  Для Linux
  
      ```
      python3 -m venv venv
      source venv/Scripts/activate
      pip3 install -r requirements.txt
      cd images_uploading
      python3 manage.py migrate
      python3 manage.py runserver
      ```
      
   Для Windows
   
      ```
      python -m venv venv
      venv\Scripts\activate.bat
      pip install -r requirements.txt
      cd images_uploading
      python manage.py migrate
      python manage.py runserver
      ```
   После выполнения команд на локальном компьютере развернется приложение, доступное по адресу: http://127.0.0.1:8000/