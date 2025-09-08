import re  # Import Python's built-in regular expressions module

# Sample text containing a phone number
text = "Contact me at 123-456-7890"

# Find all sequences of digits in the text using regex pattern '\d+'
# '\d' matches any digit, '+' means one or more digits in a row
digits = re.findall(r"\d+", text)
print(digits)  # Output: ['123', '456', '7890']

# Replace every single digit in the text with 'X'
# '\d' matches any digit, so each digit is replaced individually
updated_text = re.sub(r"\d", "X", text)
print(updated_text)  # Output: 'Contact me at XXX-XXX-XXXX'
