# Create a Python script that has three variables: ip_addr1, ip_addr2,
# ip_addr3 (representing three corresponding IP addresses). Print these
# three variables to standard output using a single print statement.
# Make your print statement compatible with both Python2 and Python3.

from __future__ import print_function
import sys
import re

x = re.compile(r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}")
address_list = {}

while True:
	try:
		addresses = input("Enter three IPs, separated by a space:")
		l = x.findall(addresses)
		print(l)
		if l:
			# smelly code, smelly code, why are they writing you?
			for i in range(1,4):
				globals()[f"ip_addr{i}"] = l[i-1]
			break
	except Exception as e:
		print(e)

print(ip_addr1, ip_addr2, ip_addr3)

# 8.8.8.8 8.8.4.4 1.1.1.1