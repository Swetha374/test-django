FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1
WORKDIR /user_management
COPY . .
RUN apt-get update 
RUN pip install -r  requirements.txt
