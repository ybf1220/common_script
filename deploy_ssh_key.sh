#!/bin/sh
###deploy ssh_key to  omc2-ioms 
IP='223 235 236 237 238 239'
for i in $IP
do
ssh Nemuadmin@10.212.247.$i 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
done
