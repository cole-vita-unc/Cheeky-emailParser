# Import the necessary modules
import re

# Define a regular expression pattern to match the tracking number
pattern = r'\b(1Z ?[0-9A-Z]{3} ?[0-9A-Z]{3} ?[0-9A-Z]{2} ?[0-9A-Z]{4} ?[0-9A-Z]{3} ?[0-9A-Z]|[\dT]\d\d\d ?\d\d\d\d ?\d\d\d)\b'

# Read the email message
message = open('test.txt').read()

# Find all matches of the tracking number in the email message
tracking_numbers = re.findall(pattern, message)

# Print the tracking numbers
print('Tracking numbers:', tracking_numbers)