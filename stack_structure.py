# Implement a stack data structure in Python.
# Test your code with boundary cases, like
# trying to remove an element from an already empty stack.
# If removing or peek an item from an empty stack,
# return None instead of throwing an exception.

class Stack:
 def __init__(self):
     # initializes Stack class
   self.objs = []

 def isEmpty(self):
   # tests if the stack is empty or not
    return self.objs == []

 def push(self, item):
   # adds the new item to the top of the stack
    self.objs.append(item)

 def pop(self):
   # removes top item from stack and returns it,
   # if the stack is empty it returns None
   if len(self.objs) == 0:
       return None
   else:
       return self.objs.pop()

 def peek(self):
   # returns the top item from the stack but it does not remove it,
   # if the stack is empty it returns None
   if len(self.objs) == 0:
       return None
   else:
       return self.objs[len(self.objs) - 1]

 def size(self):
   # returns num of items in the stack
   return len(self.objs)


# Code to test Stack class
s = Stack()
s.push(15)
s.push(22)
s.push(37)
s.push(4)
s.push(11)

while not s.isEmpty():
    print(s.pop())