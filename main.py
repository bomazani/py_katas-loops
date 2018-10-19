#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
"""
Python 2.7 Katas Loops

You will create a single file for all these exercises. 
Each individual exercise should print its result to the console. 
Use a "for" loop for each exercise.
NOTE: follow this pattern in your file for ease of grading
and checking your own work:
print ' 1. ----------------------------'
# code for 1. goes here.
print ' 2. ----------------------------'
# code for 2. goes here

author: bobh
"""


sampleArray = [469, 755, 244, 245, 758, 450, 302, 20, 712,
               71, 456, 21, 398, 339, 882, 848, 179, 535, 940, 472]

print('1. Print the numbers from 1 to 20.')
for i in range(1, 21):
    print(i)

print('2. Print the even numbers from 1 to 20.')
for i in range(0, 21, 2):
    print(i)

print('3. Print the odd numbers from 1 to 20.')
for i in range(1, 21, 2):
    print(i)

print('4. Print the multiples of 5 up to 100.')
for i in range(0, 100, 5):
    print(i)

print('5. Print the square numbers up to 100.')


def is_square5(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        print(i)


for i in range(1, 101):
    is_square5(i)

print('6. Print the numbers counting backwards from 20 to 1.')
for i in range(20, 0, -1):
    print(i)

print('7. Print the even numbers counting backwards from 20.')
for i in range(20, 0, -1):
    if not i % 2:
        print(i)

print('8. Print the odd numbers from 20 to 1, counting backwards.')
for i in range(20, 0, -1):
    if i % 2:
        print(i)

print('9. Print the multiples of 5, counting down from 100.')
for i in range(100, 0, -1):
    if not i % 5:
        print(i)

print('10. Print the square numbers, counting down from 100.')


def is_square10(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        print(i)


for i in range(101, 0, -1):
    is_square10(i)

print('11. Print the 20 elements of sampleArray.')
for i in range(0, len(sampleArray)):
    print(sampleArray[i])

print('12. Print all the even numbers contained in sampleArray.')
for i in range(0, len(sampleArray)):
    if not sampleArray[i] % 2:
        print(sampleArray[i])

print('13. Print all the odd numbers contained in sampleArray.')
for i in range(0, len(sampleArray)):
    if sampleArray[i] % 2:
        print(sampleArray[i])

print('14. Print the square of each element in sampleArray.')
for i in range(0, len(sampleArray)):
    print(sampleArray[i] ** 2)

print('15. Print the sum of all the numbers from 1 to 20.')
sum15 = 0
for i in range(1, 21):
    sum15 += i
print(sum15)

print('16. Print the sum of all the elements in sampleArray.')
sum16 = 0
for i in range(0, len(sampleArray)):
    sum16 += sampleArray[i]
print(sum16)

print('17. Print the smallest element in sampleArray.')
answer17 = sampleArray[0]
for i in range(0, len(sampleArray)):
    if sampleArray[i] < answer17:
        answer17 = sampleArray[i]
print(answer17)

print('18. Print the largest element in sampleArray.')
answer18 = sampleArray[0]
for i in range(0, len(sampleArray)):
    if sampleArray[i] > answer18:
        answer18 = sampleArray[i]
print(answer18)
