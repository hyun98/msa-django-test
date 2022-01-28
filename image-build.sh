#!/bin/bash

docker build -t profile ./profile/
echo "profile image build success!"

docker build -t apigateway ./apigateway/
echo "apigateway image build success!"

docker-compose 