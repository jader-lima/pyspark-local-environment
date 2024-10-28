# Base image
FROM docker.io/bitnami/spark:3.5

# using root user for installs
USER root

# Updating packages and dependencies 
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file from host system to container
COPY requirements.txt /tmp/requirements.txt

# Install libs listed in  requirements.txt file 
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Adjusting permissions 
USER 1001

# setting workspace as same as the baseimage  
WORKDIR /opt/bitnami/spark
