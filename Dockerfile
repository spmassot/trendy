FROM python:3.8-slim as builder

# Create app directory
WORKDIR /app

COPY app .

# Install app dependencies
RUN pip install -r requirements.txt
