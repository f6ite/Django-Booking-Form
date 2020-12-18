FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py createsuperuser

COPY . /app
