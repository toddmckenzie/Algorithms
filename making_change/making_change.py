#!/usr/bin/python

import sys

total = 0

def making_change(amount, denominations):
  global total
  if amount < 0:
    return -1
  if amount == 0: 
    total += 1
    print('total is ' + str(total))
  else:
    for i in denominations:
      if amount - i >= 0:
        print(amount, i)
        making_change(amount - i, denominations)
  
  return total



# def making_change(amount, denominations):
#   total = 0
#   if amount == 0:
#     total += 1
#   else:
#     for i in denominations:
#       if amount - i >= 0:
#         print(amount, i)
#         making_change(amount - i, denominations)
  
#   return total

denominations = [1, 5, 10, 25, 50]
# print(making_change(5, denominations)) 
# print(making_change(0, denominations)) 
# print(making_change(5, denominations)) 
print(making_change(10, denominations))
# print(making_change(20, denominations))