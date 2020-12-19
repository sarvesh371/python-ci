# Get Base image
FROM python:latest

# Maintain Label
LABEL maintainer="Sarvesh Singh <sarveshsingh.03@gmail.com>"
ARG IMAGE_NAME='sarvesh030195/python-automation:v1'
ENV DEBIAN_FRONTEND=noninteractive \
    JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64" \
    PATH=$PATH:/usr/local/bin

# Set working directory
USER root
WORKDIR /root

# Essential Packages/Setup
RUN apt-get --assume-yes update && \
    apt --assume-yes install default-jre default-jdk && \
    apt-get --assume-yes install build-essential libssl-dev python3-dev && \
    curl -o allure-2.7.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz && \
    tar -zxvf allure-2.7.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure && \
    rm -rf allure-*

# Copy Code
COPY ./requirements.txt ./

# Run Code
RUN export PYTHON_VENV=venv && \
    rm -rf $PYTHON_VENV && \
    python3 -m pip install -U pip && \
    python3 -m pip install -U virtualenv && \
    python3 -m virtualenv $PYTHON_VENV && \
    . /root/$PYTHON_VENV/bin/activate && \
    python3 -m pip install --progress-bar pretty --requirement requirements.txt && \
    deactivate

# Remove files
RUN rm -rf requirements.txt