Python 3.10
# обновляю pip
python.exe -m pip install --upgrade pip
pip install -r requirements.txt 
# создаю виртуальное окружение через vscode -> .venv
# активация виртуального окружения
source .venv/Scripts/activate
# установка Django сразу последней версии
pip install Django==4.2

django-admin startproject myshop
cd myshop/
django-admin startapp shop

+ установка Microsoft C++ Build Tools https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/
pip install Pillow==2.9.0
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
rin
rin@mail.ru
8219rin

+ pip install pytz

python manage.py runserver

# формирую файл зависимостей проекта
+ pip freeze > requirements.txt
# обновить до последней версии
pip install --upgrade pillow
# устанавливаю последнюю версию
pip install celery==5.4.0


# скачиваю rabbitmq-server-windows-3.13.3 и распаковываю в C:\Program Files
Открываю Командную строку под админом и устанавливаю
# а для него еще и Chocolate
C:\Windows\system32>@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
# установить для его работы Erland
C:\Windows\system32>choco install erlang
# там же в Командной строке перехожу к месту размещения папки
cd C:\Program Files\rabbitmq_server-3.13.3\sbin
и запускаю
rabbitmq-server

# в другом терминале запускаю celery
Rin@RINka MINGW64 /c/Dev/mtuci_practic/myshop
celery -A myshop worker -l info

pip install flower

# запускаю и этот, не закрывая предыдущий
Rin@RINka MINGW64 /c/Dev/mtuci_practic/mysho
celery -A myshop flower

# создаем новое приложение
python manage.py startapp coupons

# запустить ngrok
./ngrok http 8000
# но сначала надо его установить - Командная строка под админом
C:\Windows\system32>choco install ngrok
поставилсся сюда C:\ProgramData\chocolatey\lib\ngrok\tools
перехожу сюда
cd C:\ProgramData\chocolatey\lib\ngrok
ngrok http 8000

# нужно выполнить
django-admin makemessages --all
# но требуется установить, качаю архив с сайта https://mlocati.github.io/articles/gettext-iconv-windows.html
сюда C:\Program Files\gettext-iconv

python.exe -m pip install --upgrade django-admin
gettext --version
добавляю путь в Изменение системных переменных среды - Переменные среды - Path - Изменить - вписываю путь C:\Program Files\gettext-iconv\lib\gettex
перезагружаю комп и работает

django-admin makemessages --all
django-admin compilemessages


pip install django-rosetta==0.7.6
+ 
python.exe -m pip install --upgrade rosetta
pip install scipy
pip install nltk
pip install pandas
pip install url
pip install patterns

python manage.py makemigrations
python manage.py migrate

# url - устарели на версии django 2, меняю на path

+ pip install django --upgrade
+ pip install --upgrade django-rosetta

pip freeze > requirements.txt
# и заработало

pip install django-parler==1.5.1
pip install --upgrade translation
pip install parler

python manage.py makemigrations shop --name "add_translation_model"

pip install --upgrade django-parler


python manage.py runserver
+ pip install reverse
+ pip install language
