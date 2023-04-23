FROM python:latest

MAINTAINER Cameron Trippick "trippickc@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev


COPY ./requirements.txt /requirements.txt

COPY ./setup.py /setup.py

COPY . /

WORKDIR /

RUN pip install .

ENV ACCESS-KEY = "Placeholder"

ENV SECRET-KEY = "Placeholder"

ENV REGION = "Placeholder"

ENV LOG-STREAM = "Placeholder"

CMD [ "Secrets-Creator" ]