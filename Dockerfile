FROM python:2.7-alpine

COPY inventory.py /opt/
COPY run.sh /opt/

RUN mkdir /var/hamwan-inventory && \
    chmod +x /opt/run.sh

ENV PORTAL_ANSIBLE_URL=https://portal.memhamwan.net/host/ansible.json
ENV HOST_GROUPS=linux,mikrotik,MemHamWAN
ENV FETCH_INTERVAL=30

VOLUME /var/hamwan-inventory/

CMD "/opt/run.sh"
