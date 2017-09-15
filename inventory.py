import json
import sys
import urllib2
import ssl

# Use this like:
# while sleep 30; do python prometheus/inventory.py https://portal.memhamwan.net/host/ansible.json linux > linux_hosts.json; done
host_group = sys.argv[1]
hosts = sys.argv[2]

context = ssl._create_unverified_context()
response = urllib2.urlopen(host_group, context=context)
content = response.read()

json_obj = json.loads(content)

output_list = []
if host_group === 'linux':
    hosts = [s + ':8080' for s in hosts]
output_list.append({'targets': json_obj[hosts], 'labels': {}})
print json.dumps(output_list)
