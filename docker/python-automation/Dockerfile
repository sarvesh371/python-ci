# Get Base image
FROM python:latest

# Maintain Label
LABEL maintainer="Sarvesh Singh <sarveshsingh.03@gmail.com>"
ARG IMAGE_NAME='sarvesh030195/python-automation:v1'

# Set working directory
WORKDIR /root

# Copy Code
COPY ./requirements.txt ./

# Run Code
RUN export PYTHONHTTPSVERIFY=0 && \
    export PYTHON_VENV=venv && \
    rm -rf $PYTHON_VENV && \
    python3 -m pip install virtualenv && \
    python3 -m virtualenv $PYTHON_VENV && \
    /bin/bash -c "source $PYTHON_VENV/bin/activate" && \
    python3 -m pip install -U pip && \
    python3 -m pip install -U virtualenv && \
    python3 -m pip install --progress-bar pretty --requirement requirements.txt