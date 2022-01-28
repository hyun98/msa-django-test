FROM python:3.9.0

COPY ./ /home/ubuntu/msa-django-test/profile

WORKDIR /home/ubuntu/msa-django-test/profile/

RUN apt-get upgrade && pip3 install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8001
