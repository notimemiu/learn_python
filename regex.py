import re
hand = open('regex_sum_206299.txt')
wordsnums = hand.read()
nums = re.findall('[0-9]+',wordsnums)
total = 0
for num in nums:
    total = total + int(num)
print total
