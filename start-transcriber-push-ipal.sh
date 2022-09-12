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

# start transcriber process on interface $INTERFACE
echo "Starting Transcriber on interface $INTERFACE"
ipal-transcriber --interface $INTERFACE --ipal.output $INTERFACE.ipal $@ &

# start server push of produced data to given server
run_push_ipal () {
  echo "waiting until IDS-Server on $SERVERIP is available"
  until tail -F $INTERFACE.ipal | ncat -w5 $SERVERIP $SERVERPORT
  do
    echo "IDS-Server not ready... retry in 1s"
    sleep 1
  done 
}
until [ "$(cat $INTERFACE.ipal)" ]
do 
  echo "waiting for first packet to be transcribed"
  sleep 1
done
run_push_ipal &

wait -n 
exit $?
