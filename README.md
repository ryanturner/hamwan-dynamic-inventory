# hamwan-dynamic-inventory
This runs a script that fetches inventory from the hamwan portal application and formats it for prometheus's file_sd. The expectation is to use volumes to get data out of this and into prometheus. There are a few handy environment variables available to tweak things; see below.

## Example use
```
docker run -v /tmp/hamwan:/var/hamwan-inventory/ -e PORTAL_ANSIBLE_URL=https://portal.memhamwan.net/host/ansible.json -e HOST_GROUPS=linux,mikrotik,MemHamWAN -e FETCH_INTERVAL=30 -it k0ret/hamwan-dynamic-inventory
```

## License
See LICENSE file.
