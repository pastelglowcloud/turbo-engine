import re

# option 1
testing = open("/Users/shrutimishra/Downloads/regex_sum_42.txt")
content = testing.read()
strings = re.findall('[0-9]+', content)
sum_1 = 0
for string in strings:
    sum_1 += int(string)
print(sum_1)

# option 2
print(sum([int(i) for i in re.findall('[0-9]+', open("/Users/shrutimishra/Downloads/regex_sum_1131164.txt").read())]))
