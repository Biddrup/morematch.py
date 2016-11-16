import re

#Will take a paragraph from user
print('Please, give me the paragraph')
a = input()

#Take the word need to be find out
print('The ward you want to find out')
b = input()

#This will find out
match = re.compile(b, re.I)
isithere = match.search(a)

#Will print the result
if isithere != None:
    print(b + ' is here')
else:
    print(b + ' is not here')
