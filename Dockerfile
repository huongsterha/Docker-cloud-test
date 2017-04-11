FROM ubuntu:xenial

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential

RUN pip3 install Flask

COPY . /src
WORKDIR /src

ENTRYPOINT [“python3”]
CMD [“unh698.py”]
