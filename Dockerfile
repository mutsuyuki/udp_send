FROM python:3.10-slim


RUN apt-get update -y
RUN apt-get install tk -y


WORKDIR /root/share