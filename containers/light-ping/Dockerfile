FROM python:3.5

ADD . /owtf
WORKDIR /owtf

RUN apt-get update && apt-get -y install nmap

ENTRYPOINT ["python", "executioner.py"]