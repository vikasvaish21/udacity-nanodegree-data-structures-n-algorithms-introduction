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

def longest_call():
    time_spent = {}
    for call in calls:
        if call[0] not in time_spent:
            time_spent[call[0]] = 0
        if call[1] not in time_spent:
            time_spent[call[1]] = 0
        time_spent[call[0]] += int(call[3])
        time_spent[call[1]] += int(call[3])
    long_call = ('None', 0)
    for num in time_spent:
        if time_spent[num] > long_call[1]:
            long_call = (num, time_spent[num])
    return long_call


longest_call = longest_call()
print("%(number)s spent the longest time, %(time)d seconds, on the phone during September 2016." %
      {'number': longest_call[0], 'time': longest_call[1]})
