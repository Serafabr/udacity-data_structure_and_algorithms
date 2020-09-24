"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Dictionary with the time spent on the phone for each number.
time_spent_phone = {}

for call in calls:
    caller, receiver, start_time, duration = call
    # Save the time spent on the phone for the caller and the receiver
    time_spent_phone[caller] = time_spent_phone.get(caller, 0) + int(duration)
    time_spent_phone[receiver] = time_spent_phone.get(receiver, 0) + int(duration)

# Get the key for the maximum value on time_spent_phone
phone_longest_time = max(time_spent_phone, key = time_spent_phone.get)

message = "{} spent the longest time, {} seconds, on the phone during September 2016."
print(message.format(phone_longest_time, time_spent_phone[phone_longest_time]))
