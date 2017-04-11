FROM ubuntu:xenial

RUN pip3 install Flask

COPY . /src
WORKDIR /src

EXPOSE 8080

RUN python3 unh698_test.py