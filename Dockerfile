## Image to base ours on
FROM debian

## Environment vrs to configure things
## Setting shell show pipenv shell works
ENV SHELL=/bin/bash

## Update and install dependencies
RUN apt update && \
  apt upgrade -y && \
  apt install python3-pip -y  && \
  pip3 install pandas scikit-learn && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-allan-gon
