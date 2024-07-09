#!/usr/bin/python
import math
import argparse

def find_max_profit(prices):
  max_profit = -10000000000000
  
  for i in range(len(prices)-1):
    k = i + 1
    while k < len(prices):
      if prices[k] - prices[i] > max_profit:
        max_profit = prices[k] - prices[i]
        k += 1
      else:
        k += 1
  return max_profit


print(find_max_profit([10, 7, 5, 8, 11, 9]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


