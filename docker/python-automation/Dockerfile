# Get Base image
FROM ubuntu:latest

# Maintain Label
LABEL maintainer="Sarvesh Singh <sarveshsingh.03@gmail.com>"
ARG IMAGE_NAME='sarvesh030195/python-automation:v1'

# Set working directory
WORKDIR /root

# Install Basic Packages
RUN apt-get --assume-yes --allow-unauthenticated clean && \
    apt-get --assume-yes --allow-unauthenticated update && \
    apt-get --assume-yes --allow-unauthenticated install apt-transport-https apt-utils bc build-essential && \
    apt-get --assume-yes --allow-unauthenticated update


# Essential Packages
RUN apt-get --assume-yes --allow-unauthenticated install libssl-dev libpq-dev musl-dev python3.9-dev python3.9-dev \
    python3-pip python3.9-dev python3.9-venv
RUN apt-get --assume-yes --allow-unauthenticated install git python3.9 && \
    ln -fs /usr/bin/python3.9 /usr/bin/python3

# Copy Code
COPY ./requirements.txt ./

# Run Code
RUN python3 -m pip install --no-cache-dir --quiet --upgrade setuptools pyopenssl shyaml pip bc yq wheel virtualenv && \
    export PYTHONHTTPSVERIFY=0 && \
    export PYTHON_VENV=venv && \
    rm -rf $PYTHON_VENV && \
    python3 -m virtualenv $PYTHON_VENV && \
    . /root/$PYTHON_VENV/bin/activate && \
    python3 -m pip install --progress-bar pretty --requirement requirements.txt && \
    deactivate

# Remove files
RUN rm -rf requirements.txt