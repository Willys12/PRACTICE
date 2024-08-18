#!/usr/bin/env python3
from collections import deque

myQueue = deque(['John', 'Mason', 'Linda', 'Dennis', 'Mason'])

myQueue.append('Greg')
myQueue.append('Ignas')

myQueue.popleft()

print('The queue after poping an element is: ', myQueue)

#for person in myQueue:
 #   print('The queue has: ', person)
