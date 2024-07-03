# Given: a natural number n >= 2 and then n different natural numbers in sequence, in each separate line.
# Task:  a program that prints the first and second numbers of a sequence.

n = int(input())
largest_1 = 0
largest_2 = 0
for _ in range(n):
    n = int(input())
    if n > largest_1:
        largest_2 = largest_1
        largest_1 = n
    elif n > largest_2:
        largest_2 = n
print(largest_1)
print(largest_2)