import re  # Import regular expressions module (not used in this snippet, but often useful for string ops)

# Demonstrating split()
sentence = "Python is fun"
words = sentence.split()  # Splits the sentence into a list of words using whitespace as the delimiter
#print(words)  # Uncomment to see: ['Python', 'is', 'fun']

# Demonstrating join()
new_sentence = "|".join(words)  # Joins the list of words into a single string, separated by '|'
#print(new_sentence)  # Uncomment to see: 'Python|is|fun'

# Demonstrating replace()
text = "I love Java"
updated_text = text.replace("Java", "Python")  # Replaces 'Java' with 'Python' in the string
#print(updated_text)  # Uncomment to see: 'I love Python'

# Demonstrating strip()
messy = "     Hello, World     "
print(messy)  # Prints the original string with leading/trailing spaces
cleaned_text = messy.strip()  # Removes leading and trailing whitespace
print(cleaned_text)  # Prints the cleaned string: