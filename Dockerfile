FROM python:3.7
MAINTAINER Karthikkannan "karthikkannan@gmail.com"
RUN pip3 install pipenv
WORKDIR /usr/src/app
COPY Pipfile ./
COPY Pipfile.lock ./
RUN set -ex && pipenv install --deploy --system
COPY . .
EXPOSE 50051
CMD [ "python", "main.py" ]
