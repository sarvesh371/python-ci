git clone https://github.com/sarvesh371/node-api-service.git
image=$(cat Dockerfile | grep "IMAGE_NAME" | cut -d "=" -f2 | sed s/\'//g)
docker build --tag $image --no-cache .