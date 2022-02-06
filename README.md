# CryptoGIF
Web-GUI based software that enables data hiding in GIF securely with the use of crypto

Instructions to run

#1 Create Virtual Environment

pip install virtualenv

python -m virtualenv venv

#2 Activate Virtual Env

Drag activate.bat from Crypto-GIF\Server\venv\Scripts (windows)


#2 Install Packages

pip install -r requirements.txt


#3 Set project directory

set FLASK_ENV=development

#4 Run App

flask run --host=0.0.0.0

#5 Use Web-GUI

Open http://127.0.0.1:5000/ in browser
