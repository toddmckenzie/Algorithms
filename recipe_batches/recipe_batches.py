#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients, total=0):
  if total == 0:
    for k,v in recipe.items():
      if k not in ingredients.keys():
        return total

  for k,v in ingredients.items():
    if k in recipe.keys():
      if recipe[k] <= v:
        ingredients[k] = v - recipe[k] 
      else:
        return total
  
  total += 1
  return recipe_batches(recipe, ingredients, total)

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, { 'milk': 300, 'butter': 150, 'flour': 25})
# recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })
# print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
# print(recipe_batches({ 'milk': 2 }, { 'milk': 200}))
# print('second')
# print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })) 
# print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 , 'butter': 25}))
# print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
# print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))