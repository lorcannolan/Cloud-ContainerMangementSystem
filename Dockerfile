# Set the base image
FROM python:2.7

# File Author / Maintainer
MAINTAINER Lorcan Nolan

# Update the sources list
RUN apt-get update

# Update the sources list
RUN apt-get -y upgrade

# Copy the application folder inside the container
ADD /myapp /myapp

# Get pip to download and install requirements:
RUN pip install -r /myapp/requirements.txt

# Expose listener port
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /myapp
RUN mkdir /data
# Set the default command to execute
# when creating a new container
CMD python container-server.py
