# Get Base image
FROM alpine

# Maintain Label
LABEL maintainer="Sarvesh Singh <sarveshsingh.03@gmail.com>"
ENV IMAGE_NAME='alpine' \
    CUSTOM_IMAGE_NAME="mongodb"

# Install software
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories && \
    echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories && \
    apk update && \
    apk add mongodb

# Configure software
VOLUME [ "/data/db" ]
WORKDIR /data
EXPOSE 27017

# Set Default commands
CMD [ "mongod" ]