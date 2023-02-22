#!/bin/bash

set -e
set -x
set -E

INTERFACE="$1" ; shift
SERVERIP="$1" ; shift
SERVERPORT="$1" ; shift

# start prometheus node exporter if present
echo "Starting Node Exporter"
if [ -f node_exporter ]; then
    ./node_exporter &
fi

mkfifo IPAL
# start transcriber process on interface $INTERFACE
echo "Starting Transcriber on interface $INTERFACE"
ipal-transcriber --interface $INTERFACE --ipal.output IPAL $@ &

ipal-state-extractor --log INFO --ipal.input IPAL --state.out $INTERFACE.state timeslice &

# tail cannot handle two file watches https://github.com/nxadm/tail/issues/30
# start server push of produced data to given server
run_push_state () {
  echo "waiting until IDS-Server on $SERVERIP is available"
  if ping $SERVERIP -c 1 -w 20
  then
    sleep 3
    tail -F $INTERFACE.state | ncat -w5 $SERVERIP $SERVERPORT
  fi 
}

until [ "$(cat $INTERFACE.state)" ]
do
  echo "waiting for first state to be transcribed"
  sleep 1
done
run_push_state

wait -n 
exit $?
