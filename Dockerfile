FROM python:3.8-slim-buster

RUN mkdir /bookhub
COPY requirements.txt /bookhub
WORKDIR /bookhub
RUN pip3 install -r requirements.txt

COPY . /bookhub

CMD [ "gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:80" ]