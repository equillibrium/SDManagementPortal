# Подготовка окружения

## Pycharm

### Windows powershell

#### Install choco

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol
= [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient)
.DownloadString('https://community.chocolatey.org/install.ps1'))

#### Install Pycharm Community

choco install PyCharm-community -y

Ссылка для ручного скачивания:
https://www.jetbrains.com/ru-ru/pycharm/download/download-thanks.html?platform=windows&code=PCC

### MacOS homebrew

brew install pycharm-ce

## Python 3.10

### Windows powershell

choco install python3 -y

Ссылка для ручного скачивания:
https://www.python.org/downloads/

### MacOS homebrew

brew install python@3.10

## Обновление pip

### Windows powershell

python -m pip install --upgrade pip

### MacOS

sudo python3 -m pip install --upgrade pip

# Запуск стенда разработки портала

### Клонируем репо

cd *ПутькПапкеПроекта*

git clone https://gitlab.corp.tass.ru/myltsev_a/sdmanagementportal.git

### Создать и активировать виртуальное окружение

python3 -m venv venv

или

python -m venv venv

#### Windows

.\venv\scripts\Activate

#### MacOS

source venv/bin/activate

### Обновить pip внутри venv

python -m pip install --upgrade pip  
или  
python3 -m pip install --upgrade pip

### Установить пакеты Джанго

pip install -r requirements.txt  
или  
python3 -m pip install -r requirements.txt

### Выполнить миграции БД

python manage.py makemigrations MainApp  
python manage.py migrate  
или  
python3 manage.py makemigrations MainApp  
python3 manage.py migrate

### Создать суперпользователя
python manage.py createsuperuser

### Запустить дев сервер

python manage.py runserver  
или  
python3 manage.py runserver

# Технологии

Python 3.10  
Django 4  
Django crispy forms  
Bootstrap 5 https://www.bootstrapcdn.com/  
FontAwesome 6 https://fontawesome.com/download  

# При создании нового проекта

django-admin startproject *projectname* *path*

cd *projectpath*

python manage.py startapp *appname*

В папке проекта в settings.py добавить InstalledApps (имя app)

