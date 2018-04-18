# NAOqi Python development environment with Docker

[NAOqi Python SDK](http://doc.aldebaran.com/2-1/dev/python/install_guide.html) running in a Docker container. The directory `./src` is mapped in the container and real-time updated, so you can develop your code on your host machine and run it from the Docker container.

## Prerequisites

- [Docker](https://www.docker.com)

## Installation

1. Clone this repo and move into the directory.
2. Download the [Python SDK for Linux](http://doc.aldebaran.com/2-1/dev/community_software.html#retrieving-software) and put it in the root of the folder with the cloned repository. The filename should be `pynaoqi-python2.7-2.1.4.13-linux64.tar.gz`.
3. Build the container `docker build -t naoqi-python .`
4. Run the container `docker run -v ``pwd``/src:/naoqi/src -it naoqi-python bash`. This will open a bash prompt from which you can execute your code from the `./src` directory.
