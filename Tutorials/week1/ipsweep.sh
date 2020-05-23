#!/bin/bash
if [ "$1" == "" ]
then 
echo "YOu forgot an IP Addr"
else
for ip in `seq 1 154` ; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
