[root@nb3ds2 ~]# cat dhcpd.sh 
#!/bin/sh
#set -x
# Configure dhcpd 

echo "Please give enodeb information."
echo -e "MAC address: \c"
read MACADDR
echo -e "IP address: \c"
read IPADDR
echo -e "Gateway: \c"
read GATEWAY
echo -e "Netmask: \c"
read NETMASK


SUBNET=`echo $GATEWAY|cut -d. -f1-3`.$((`echo $GATEWAY|cut -d. -f4`-1))

echo
echo "Will configure the following parameters:"
echo "MAC address: $MACADDR"
echo "IP address: $IPADDR"
echo "Sub network: $SUBNET"
echo "Netmask: $NETMASK"
echo "Gateway: $GATEWAY"
echo
echo -e "Is this OK? (y/n) \c"
read CORRECT
test "$CORRECT" = "y" || { echo "Please re-run this script and enter the correct parameters"; exit 1; }

SERVER_IP=`/sbin/ifconfig bond0|grep -oP '(?<=addr:)[\d\.]+'`

cat >/etc/dhcpd.conf  <<EOF
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp*/dhcpd.conf.sample
#
server-identifier $SERVER_IP;
not authoritative;
one-lease-per-client on;
ddns-update-style none;

option vendor-encapsulated-options code 43 = string;

   class "TDDLTESYVE" {
      match if option vendor-class-identifier = "NSNBTS01";
   }
   default-lease-time 1200;
   max-lease-time 1200;
   min-lease-time 1200;

   subnet $SUBNET netmask $NETMASK {
        option routers                  $GATEWAY;
        
        #pool {
        #      allow members of "TDDLTESYVE"; 
        #      range dynamic-bootp  $IPADDR;
        #}

        ### option vendor-encapsulated-options 00:00:00:00:01:04:0A:D4:C1:48;
        host ENB_MAC_BINDING { hardware ethernet $MACADDR; fixed-address $IPADDR; }
   }


    subnet 10.212.193.0 netmask 255.255.255.128{}

EOF

echo
echo 'DHCP Server will restart in 2 seconds!'
echo
sleep 2

service dhcpd restart

if [ $? -ne 0  ];then
  echo 
  echo "parameters not correct!Please re-run this script and enter the correct parameters!"
  echo
  exit 28;
else 
  echo 
  echo "DHCP Server Restart Successfully!"
  echo
fi
