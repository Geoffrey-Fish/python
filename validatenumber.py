import re
# I simply don get that fucking regex stuff
validate = r"^[189][0-9]{7}$"
phone_number = input()
valid = re.search(validate, phone_number)
if valid:
	print("Valid")
else:
   print("Invalid")
