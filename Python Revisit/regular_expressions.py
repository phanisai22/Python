import re

# message = "Call me at 91 9759 775 290 or to my office at 91 8776 447 525"

# phone_number_extract = re.compile(r'\d\d \d\d\d\d \d\d\d \d\d\d')
# phone_numbers = phone_number_extract.search(message)
# print(phone_numbers.group())
#
# phone_numbers = phone_number_extract.findall(message)
# print(phone_numbers)
#

# bat_regrex = re.compile(r'Batman|Batwoman|Birdman|Birdwomen')

# mo = bat_regrex.search("The adventures of Birdman")
# print(mo.group())

# mo = bat_regrex.search("The adventures of BirdMan")
# print(mo == None)

bat_regrex = re.compile(r"Bat(wo)?man")
mo = bat_regrex.search("The adventures of Batman")
print(mo.group())


