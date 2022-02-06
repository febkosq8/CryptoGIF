## **Instructions to run locally**

# ***Prerequisites***

*1. Python v3.8.4*
*2. pip*
*3. Terminal*

>Open Windows Terminal / Command Prompt on the server root folder

### #1 Create Virtual Environment

```
pip install virtualenv

python -m virtualenv venv
```

### #2 Activate Virtual Env

>Drag activate.bat from Crypto-GIF\Server\venv\Scripts (windows)

### #3 Install Packages

```
pip install -r requirements.txt
```

### #4 Set project directory

```
set FLASK_ENV=development
```

### #5 Run App

```
flask run --host=0.0.0.0
```

### #6 Use Web-GUI

>Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in browser
