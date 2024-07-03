# Given: two natural numbers as input - a and b (a < b). 
# Task:  write a program that finds the natural number from the segment with the maximum sum of divisors.
# Note:  if there are several numbers with the maximum sum of divisors, then the required number is the largest of them. 
#        program should output the response in the following format:
#        <number with the maximum sum of divisors> <sum of divisors of this number>

a = int(input())
b = int(input())
total = 0
largest = 0

for i in range(a, b + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += j
        if counter >= total:
            total = counter
            largest = i
print(largest, total)