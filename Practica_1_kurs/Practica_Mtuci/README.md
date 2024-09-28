Python 3.10
mkdir env
pip install virtualenv
python.exe -m pip install --upgrade pip # обновляю pip
virtualenv env/myshop # создаю виртуальное окружение
source env/myshop/Scripts/activate # активация виртуального окружения
pip install Django==1.8.6 # установка Django
pip install --upgrade django==4.2
django-admin startproject myshop
cd myshop/
django-admin startapp shop

+ установка Microsoft C++ Build Tools https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/
pip install Pillow==2.9.0
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
rin
rin@maiil.ru
8219rin

+ pip install pytz
+ python manage.py collectstatic

python manage.py runserver
