#!/usr/bin/python

# Read CIDR ranges from file and expand IPs
# IPs will duplicate if there are overlapping networks. 
# Run "sort -u" on the output to remove dups.

from iptools import IpRangeList

def clean(ip_string):

	ret = ip_string.strip()
	if "-" in ret:
		parts = ret.split("-")
		ret = (parts[0], ret.rsplit(".", 1)[0] + "." + parts[1])

	return ret

with open("CIDRrange.txt", "r") as file_in:
	in_list = [clean(x) for x in file_in.readlines()]

ips_and_ranges = IpRangeList(*in_list)

with open("IPs.txt", "w") as file_out:
	for ip in ips_and_ranges:
		file_out.write(ip + '\n')
