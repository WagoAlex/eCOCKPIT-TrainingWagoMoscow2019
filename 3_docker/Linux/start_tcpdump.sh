#!/bin/bash

# Eckhard
# Version: 1.0
# 14.12.2018 after copying this file to /home/codesys 
# it has to be set executable 

# Execute tcpdump command silently (2>/dev/null suppresses errors)
/usr/bin/nohup /usr/sbin/tcpdump -i br0 -n -w /media/sd/dump2.pcap 2>/dev/null &
echo "recording started"
