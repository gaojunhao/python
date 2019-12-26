from collections import deque
# list function
list_1 = [1, 's', 5, (20, 45)]
list_1.append('c')
print(list_1)
list_2 = [(1, 'a'), 'L']
list_1.append(list_2)
print(list_1)

# like stack
print(list_1.pop())

#like queue
queue = deque(list_1)
print(queue.popleft())
