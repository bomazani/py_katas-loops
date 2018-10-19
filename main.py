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
answerArray1 = []
for i in range(1, 21):
    answerArray1.append(i)
print(answerArray1)

print('2. Print the even numbers from 1 to 20.')
answerArray2 = []
for i in range(1, 21):
    if i % 2:
        continue
    else:
        answerArray2.append(i)
print(answerArray2)

print('3. Print the odd numbers from 1 to 20.')
answerArray3 = []
for i in range(1, 21):
    if i % 2:
        answerArray3.append(i)
print(answerArray3)

print('4. Print the multiples of 5 up to 100.')
answerArray4 = []
for i in range(1, 101):
    if i % 5 == 0:
        answerArray4.append(i)
print(answerArray4)

print('5. Print the square numbers up to 100.')
answerArray5 = []


def is_square5(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        answerArray5.append(i)


for i in range(1, 101):
    is_square5(i)
print(answerArray5)

print('6. Print the numbers counting backwards from 20 to 1.')
answerArray6 = []
for i in range(20, 0, -1):
    answerArray6.append(i)
print(answerArray6)

print('7. Print the even numbers counting backwards from 20.')
answerArray7 = []
for i in range(20, 0, -1):
    if not i % 2:
        answerArray7.append(i)
print(answerArray7)

print('8. Print the odd numbers from 20 to 1, counting backwards.')
answerArray8 = []
for i in range(20, 0, -1):
    if i % 2:
        answerArray8.append(i)
print(answerArray8)

print('9. Print the multiples of 5, counting down from 100.')
answerArray9 = []
for i in range(100, 0, -1):
    if not i % 5:
        answerArray9.append(i)
print(answerArray9)

print('10. Print the square numbers, counting down from 100.')
answerArray10 = []


def is_square10(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        answerArray10.append(i)


for i in range(101, 0, -1):
    is_square10(i)
print(answerArray10)

print('11. Print the 20 elements of sampleArray.')
answerArray11 = []
for i in range(0, len(sampleArray)):
    answerArray11.append(sampleArray[i])
print(answerArray11)

print('12. Print all the even numbers contained in sampleArray.')
answerArray12 = []
for i in range(0, len(sampleArray)):
    if not sampleArray[i] % 2:
        answerArray12.append(sampleArray[i])
print(answerArray12)

print('13. Print all the odd numbers contained in sampleArray.')
answerArray13 = []
for i in range(0, len(sampleArray)):
    if sampleArray[i] % 2:
        answerArray13.append(sampleArray[i])
print(answerArray13)

print('14. Print the square of each element in sampleArray.')
answerArray14 = []
for i in range(0, len(sampleArray)):
    square = sampleArray[i] ** 2
    answerArray14.append(square)
print(answerArray14)

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
