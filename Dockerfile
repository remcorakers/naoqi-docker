FROM ubuntu:17.10

# Install dependencies
RUN apt-get update && apt-get install -y python-pip iproute2 telnet

# Set the working directory to /naoqi
WORKDIR /naoqi

# Copy the NAOqi for Python SDK
ADD pynaoqi-python2.7-2.1.4.13-linux64.tar.gz /naoqi/

# Copy the boost fix
# See https://community.ald.softbankrobotics.com/en/forum/import-issue-pynaoqi-214-ubuntu-7956
ADD boost/* /naoqi/pynaoqi-python2.7-2.1.4.13-linux64/

# Set the path to the SDK
ENV PYTHONPATH=${PYTHONPATH}:/naoqi/pynaoqi-python2.7-2.1.4.13-linux64/
ENV LD_LIBRARY_PATH="/naoqi/pynaoqi-python2.7-2.1.4.13-linux64:$LD_LIBRARY_PATH"

# Copy the source folder
COPY ./src /naoqi/src
