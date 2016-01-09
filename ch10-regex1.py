import re

name = "regex_sum_190854.txt"
handle = open(name)
count = 0
numbers = []
for line in handle:
  numbers += line.rstrip().split()

matches = []
for n in numbers:
  matches += re.findall('[0-9]+', n)

total = 0
for m in matches:
  total += int(m)

print total