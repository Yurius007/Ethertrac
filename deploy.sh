#!/bin/bash

echo "Stopping existing container..."
sudo docker stop ethertrac-flask-app && sudo docker rm ethertrac-flask-app

echo "Removing old image..."
sudo docker rmi -f yurius007/ethertrac-flask:1.01.RELEASE

echo "Pulling latest image..."
sudo docker pull yurius007/ethertrac-flask:1.01.RELEASE

echo "Starting new container..."
sudo docker run -i -d -t -p 80:80 --name ethertrac-flask-app yurius007/ethertrac-flask:1.01.RELEASE

echo "Deployment complete!"