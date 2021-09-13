# Prompt a user to enter in an IP address from standard input. Read the IP
# address in and break it up into its octets. Print out the octets in decimal,
# binary, and hex.
# Four columns, fifteen characters wide, a header column, data centered in the column.

import re

x = re.compile(r"""
	(25[0-5]|2[0-4][0-9]|1?\d\d?)(?:\.)
	(25[0-5]|2[0-4]\d|[01]?\d\d?)(?:\.)
	(25[0-5]|2[0-4]\d|[01]?\d\d?)(?:\.)
	(25[0-5]|2[0-4]\d|[01]?\d\d?)
	""", re.VERBOSE)

octet_dict = {}

while True:
	try:
		address = input("Please enter an IP address:")
		m = x.match(address)
		if m != None:
			for i in range(1,5):
				octet_dict[f"octet{i}"] = m.group(i)
			break
		else:
			print("That doesn't look like an IP.")
	except Exception as e:
		print(e)

def display(octet_dict):
	print("")
	
	for j in range(1,5):
		print('{: ^15}'.format(f"Octet{j}"), end="")

	print("")
	print("-" * 60)

	for k in range(1,5):
		octet_int = octet_dict[f"octet{k}"]
		print('{: ^15}'.format(octet_int), end="")

	print("")

	for l in range(1,5):
		octet_bin = int(octet_dict[f"octet{l}"])
		print('{: ^#15b}'.format(octet_bin), end="")

	print("")

	for n in range(1,5):
		octet_hex = int(octet_dict[f"octet{n}"])
		print('{: ^#15x}'.format(octet_hex), end="")

	print("")
	print("-" * 60)

display(octet_dict)