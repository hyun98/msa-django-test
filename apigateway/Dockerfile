FROM python:3.9.0

COPY ./ /home/ubuntu/msa-django-test/apigateway

WORKDIR /home/ubuntu/msa-django-test/apigateway/

RUN apt-get upgrade && pip3 install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000
