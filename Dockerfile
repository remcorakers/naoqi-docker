FROM --platform=amd64 ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y python2-minimal iproute2 telnet iputils-ping

# Set the working directory to /naoqi
WORKDIR /naoqi

# Copy the NAOqi for Python SDK
ADD pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327.tar.gz /naoqi/

# Copy the boost fix
# See https://community.ald.softbankrobotics.com/en/forum/import-issue-pynaoqi-214-ubuntu-7956
COPY boost/* /naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/

# Set the path to the SDK
ENV PYTHONPATH=${PYTHONPATH}:/naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/lib/python2.7/site-packages/
ENV LD_LIBRARY_PATH="/naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327:$LD_LIBRARY_PATH"

# Copy the source folder
COPY ./src /naoqi/src
