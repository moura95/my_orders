FROM python:3.9

COPY . /opt/app/core

WORKDIR /opt/app/core

EXPOSE 8000

CMD ["make", "migrate", "runserver"]
