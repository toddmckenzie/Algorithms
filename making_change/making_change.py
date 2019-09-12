#!/usr/bin/python

import sys

def making_change(amount, denominations):
  total = 0
  if amount < 0:
    return -1
  if amount == 1 or amount == 0:
    total += 1
  else:
    for i in denominations:
      print(i)
      if amount - i >= 0:
        print('here is amount and i')
        print(amount, i)
        making_change(amount - i, denominations)
  
  return total

denominations = [1, 5, 10, 25, 50]

making_change(5, denominations)

# if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  # if len(sys.argv) > 1:
  #   denominations = [1, 5, 10, 25, 50]
  #   amount = int(sys.argv[1])
  #   print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  # else:
  #   print("Usage: making_change.py [amount]")