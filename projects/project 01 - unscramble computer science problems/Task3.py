"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A: All called prefixes (and area codes)
called_prefixes = set()
# Part B: total calls from Bangalore and total calls from Bangalore to Bangalore
calls_from_bangalore = 0
calls_to_bangalore = 0

# Get area code from telephone number
def get_area_code(phone):
    final_index = phone.find(")")
    area_code = phone[0 : final_index + 1]
    if area_code:
      return area_code
    return None

for call in calls:
    caller, receiver, start_time, duration = call
    # If the caller is from Bangalore
    if "(080)" in caller:
        calls_from_bangalore += 1
        # If it's calling a mobile
        if receiver[0] in ("7", "8", "9"):
            called_prefixes.add(receiver[0:4])
        # If it's calling a telemarketer number
        if receiver[0:3] == "140":
            called_prefixes.add(receiver[0:3])
        # If it's calling a fixed lines
        elif receiver[0] == '(':
            called_prefixes.add(get_area_code(receiver))
            if "(080)" in caller:
              calls_to_bangalore += 1

# Part A answer
#The list of codes should be print out one per line in lexicographic order with no duplicates.
print("The numbers called by people in Bangalore have codes:")
called_prefixes = sorted(list(called_prefixes))
for code in called_prefixes:
  print(code)

# Part B answer
# The percentage should have 2 decimal digits
message = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
print(message.format(round(calls_to_bangalore / calls_from_bangalore, 2)))