FROM ubuntu:xenial
FROM python:3-onbuild

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential

RUN pip3 install Flask

COPY . /src
WORKDIR /src

EXPOSE 5000
CMD[“python”,”unh698_test.py”]
