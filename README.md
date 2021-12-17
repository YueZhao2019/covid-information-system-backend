## Version
django<2.0

djangorestframework==3.8.1


## Step 0: Download code and goto project
```
$ git clone https://github.com/YueZhao2019/covid-information-system-backend.git
$ cd covid-information-system-backend
```

## Step 1: Installation dependency
```
$ pip install -r requirements.txt
```

## Step 2 ：Make database migrations and fill in the data
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Step 3 ：Run
```
$ python manage.py runserver
Open the browser: http://127.0.0.1:8000/
```


## Different accounts to login system

```
Administrator   // username:aa01     password:123456
Student   // username:2499059z     password:123456
Teacher   // username:tt01     password:123456

```
