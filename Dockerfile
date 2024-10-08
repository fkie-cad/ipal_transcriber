FROM ubuntu:latest

RUN apt-get update \
    && apt-get -y install software-properties-common sudo g++ \
    && apt-get -y install pip vim
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tshark

# create a user and add them to sudoers
RUN useradd -ms /bin/bash ipal && echo "ipal ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ipal
USER ipal

WORKDIR /home/ipal/ipal_transcriber/
COPY --chown=ipal . .

# Install transcriber
RUN sudo pip install --break-system-packages .
RUN sudo pip install --break-system-packages -r requirements-dev.txt

CMD /bin/bash
