FROM ubuntu:22.04

RUN apt-get update
RUN uname -a
RUN apt-get -y install linux-headers-5.15.0-37-generic
RUN apt-get -y install software-properties-common sudo g++
RUN apt-get -y install pip vim
RUN apt-get -y install iproute2 iputils-ping ncat
RUN apt-get -y install jq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tshark

# create a user and add them to sudoers
# RUN useradd -ms /bin/bash ipal && echo "ipal ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ipal
# USER ipal

WORKDIR /home/ipal/ipal_transcriber/
# COPY --chown=ipal . .
COPY . .

# Install transcriber
RUN sudo pip install .
RUN sudo pip install -r requirements-dev.txt

CMD "/bin/bash"
