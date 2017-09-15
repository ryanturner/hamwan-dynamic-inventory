#!/bin/sh
while sleep ${FETCH_INTERVAL}
do
  for i in $(echo ${HOST_GROUPS} | sed "s/,/ /g")
  do
    python /opt/inventory.py ${PORTAL_ANSIBLE_URL} ${i} > /var/hamwan-inventory/${i}_hosts.json
  done
done
