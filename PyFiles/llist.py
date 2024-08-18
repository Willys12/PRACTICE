#!/usr/bin/env python3

def process_food():
	food = ['pizza', 'rice', 'spaghetti', 'BBQ', 'burger', 'fries', 'BBQ']
	#print(food[2])
	food.append('cake')
	food.insert(2, 'ice cream')
	food.pop(3)
	food.reverse()
	return food

result = process_food()
print(result)