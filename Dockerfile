FROM ubuntu:xenial

RUN pip install Flask

COPY . /src
WORKDIR /src

EXPOSE 8080

RUN python3 unh698_test.py