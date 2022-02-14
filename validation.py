import yaml
import sys
import os
def validate(input_file, hosts_file):
    input = open(hosts_file).read()
    f = open(input_file)
    hostnames = yaml.load(f, Loader=yaml.BaseLoader)['variable_host']
    if not hostnames:
        print("Hosts name is empty")
        return False
    for line in hostnames:
        if not line in input:
            print("Error: {} not in hosts.Please check your input parameter configmap with hosts configmap, whether you are passing a same cluster details".format(line))
            return False
    print("Successfully validated find yaml")
    return True

if __name__ == '__main__':
    input_file = sys.argv[1]
    hosts_file = sys.argv[2]
    if validate(input_file, hosts_file):
        sys.exit(0)
    else:
        sys.exit(1)
