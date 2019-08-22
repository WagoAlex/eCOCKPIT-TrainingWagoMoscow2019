#!/bin/bash

# Eckhard
# Version: 1.0
# 14.12.2018 after copying this file to /home/codesys 
# this script has to be set executable 

# Stop tcpdump without error messages (silently)
killall tcpdump 2>/dev/null
echo "recording stopped"

# or a bit more polite: get the pid (process id) and stop only this process
# PID=$(/usr/bin/ps -ef | grep tcpdump | grep -v grep | grep -v ".sh" | awk '{print $2}')
# /usr/bin/kill -9 $PID
