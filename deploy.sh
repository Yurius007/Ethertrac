#!/bin/bash

CONTAINER_NAME="ethertrac-flask-app"
IMAGE_NAME="yurius007/ethertrac-flask:1.01.RELEASE"

echo "Checking if container '$CONTAINER_NAME' exists..."
if [ "$(sudo docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    if [ "$(sudo docker ps -q -f name=$CONTAINER_NAME)" ]; then
        echo "Stopping running container..."
        sudo docker stop $CONTAINER_NAME
    else
        echo "Container exists but is not running."
    fi
    echo "Removing container..."
    sudo docker rm $CONTAINER_NAME
else
    echo "No existing container found."
fi

echo "Removing old image..."
sudo docker rmi -f $IMAGE_NAME

echo "Pulling latest image..."
sudo docker pull $IMAGE_NAME

echo "Starting new container..."
sudo docker run -i -d -t -p 80:80 --name $CONTAINER_NAME $IMAGE_NAME

echo "Deployment complete!"