import json
import sys
import urllib2
import ssl

# Use this like:
# while sleep 30; do python prometheus/inventory.py https://portal.memhamwan.net/host/ansible.json linux > linux_hosts.json; done
url = sys.argv[1]
host_group = sys.argv[2]

context = ssl._create_unverified_context()
response = urllib2.urlopen(url, context=context)
content = response.read()

json_obj = json.loads(content)

output_list = []
hosts = json_obj[host_group]
if host_group == 'linux':
    hosts = [s + ":8080" for s in hosts]
output_list = [{'targets': hosts, 'labels': {}}]
print json.dumps(output_list)
