# pull official base image
FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
