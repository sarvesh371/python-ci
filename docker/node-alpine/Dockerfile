# Get Base image
FROM node:alpine

# Maintain Label
LABEL maintainer="Sarvesh Singh <sarveshsingh.03@gmail.com>"
ARG IMAGE_NAME='sarvesh030195/node-alpine:v1'

# Set working directory
WORKDIR /usr/nodeapp

# Copy Code
COPY ./node-api-service ./

# Set working directory
WORKDIR /usr/nodeapp/test2/

# Run Code
RUN npm install
CMD [ "npm", "start" ]