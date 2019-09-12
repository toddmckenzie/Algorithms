#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  choices = ['rock', 'paper', 'scissors']
  options = []
  def inner(n, items=[]):
    if n == 0:
      return options.append(items)
    for i in choices:
      inner(n-1, items + [i])
  
  inner(n, [])
  return options



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')