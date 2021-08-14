FROM python:3.8-slim-buster

RUN mkdir /bookhub
COPY requirements.txt /bookhub
WORKDIR /bookhub
RUN pip3 install -r requirements.txt

COPY . /bookhub

RUN chmod u+x ./entrypoint.sh 
ENTRYPOINT ["sh", "./entrypoint.sh"]