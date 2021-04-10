# Implement a queue data structure in Python.
# Test your code with boundary cases, like trying
# to remove an element from an already empty queue.
# If removing an item from an empty queue, return
# None instead of throwing an exception

class Queue:
  def __init__(self):
    # initializing Queue class
    self.objs = []

  def isEmpty(self):
    # tests if the queue is empty or not
    return self.objs == []

  def enqueue(self, item):
    # adds the new item to the end of the queue
    self.objs.insert(0,item)

  def dequeue(self):
    # removes and returns the first item in the queue (in the front),
    # if the queue is empty then return None
    if len(self.objs) == 0:
      return None
    else:
      return self.objs.pop()

  def size(self):
    # returns the num of items in the queue
    return len(self.objs)

# Code to test Queue class
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())