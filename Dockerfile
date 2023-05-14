FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /moneytransferAPI

WORKDIR /moneytransferAPI

COPY . /moneytransferAPI/

RUN pip install -r requirements.txt

