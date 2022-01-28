#!/bin/bash

docker-compose -f profile/docker-compose.yml down
docker-compose -f apigateway/docker-compose.yml down