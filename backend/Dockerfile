# pull official base image
FROM python:3.8.10-buster

# setting the work directory
WORKDIR /backend

RUN apt update

# installing dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

# copy project
COPY ./src/ ./

EXPOSE 8000