from __future__ import print_function
import re

# You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings.

arplist = [mac1, mac2, mac3]

for i in range(0, len(arplist)):
	arplist[i] = re.split(r"\s+", arplist[i])
	print(arplist[i])

# We want the items at indices 1 and 3 from each member of arplist.

# We're going to use str.rjust(width[, fillchar]) with a width of 20 and no argument for fillchar

def display(arplist):
	print('IP ADDR'.rjust(20), 'MAC ADDRESS'.rjust(20))
	print("-"*20, "-"*20)
	for x in arplist:
		print(x[1].rjust(20), x[3].rjust(20))

display(arplist)