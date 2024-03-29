FROM python:3.10-slim-buster

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0:8000
