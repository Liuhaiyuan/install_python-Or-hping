#!/bin/bash

IP_ADDRESS="122.112.203.101"

#ping $IP_ADDRESS  | awk '{ print $0"\t" strftime("%Y-%m-%d-%H:%M:%S",systime()) }' > /var/log/ping_log/${IP_ADDRESS}"_ping_log".log 
ping $IP_ADDRESS  | awk '{ print $0"\t" strftime("%Y-%m-%d-%H:%M:%S",systime()) }' > ${IP_ADDRESS}"_ping_log".log 

