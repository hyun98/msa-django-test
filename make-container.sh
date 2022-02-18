#!/bin/bash

docker-compose -f profile/docker-compose.yml up -d
docker-compose -f apigateway/docker-compose.yml up -d