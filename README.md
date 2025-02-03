# Chat Application

## Project Setup Instructions

## Prior Installation

# 1. Install Virtual Environment if not installed

```
pip install virtualenv
```

# 2. Enable Virtual Environment

```
python -m venv venv
```

# 3. Activate Virtual Environment

```
venv\Scripts\activate
```

# 4. Install Django

```
pip install Django
```

# 5. Verify Django Installation

```
python -m django --version
```

# 6. Install Dependancies
```
django==5.1.5
python==3.13.0
channels==4.2.0
daphne==4.1.2
```

```
pip install -r requirements.txt
```

# 7. Make Migrations
```
python manage.py makemigrations
```

# 8. Migrate DataBase
```
python manage.py migrate
```

# 9. Run Application
```
python manage.py runserver
```