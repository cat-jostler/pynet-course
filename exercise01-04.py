
import re

#Create a show_version variable that contains the following

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

# Remove all leading and trailing whitespace from the string.
x = re.compile(r"^[\w*]+?\s+") #match the first stretch of whitespace and anything before it
sv = re.sub(x, "", show_version).rstrip()

# Split the string and extract the model and serial_number from it.

model = sv.split(" ")[0]
serial_number = sv.split(" ")[-1] # didn't work with [1]

# Check if 'Cisco' is contained in the model string (ignore capitalization).

if model.lower().find("cisco") != -1:
	print("Found it.")

# Check if '881' is in the model string.

if model.lower().find("881") != -1:
	print("Found it.")
	
# Print out both the serial number and the model.
print("Model        : " + model)
print("Serial number: " + serial_number)