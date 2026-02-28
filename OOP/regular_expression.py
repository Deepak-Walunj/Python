import re

pattern = r'a'
text = "cat"
match = re.search(pattern, text)
print(match)
# print(match.group())  # Output: a

pattern = r'.'
text = "cat"
match = re.search(pattern, text)
print(match)

match=re.finditer(r'\d+', 'There are 24 hours in a day and 60 minutes in an hour')
print(match)