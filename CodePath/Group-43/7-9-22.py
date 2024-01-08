class Stack:
  def __init__(self):
    self.stack = []

  def push(self, int):
    self.stack.append(int)

  def pop(self):
    self.stack.pop

  def peek(self):
    x = self.stack[-1]
    return x

  def isEmpty(self):
    if len(self.stack) == 0:
      return True
    return False

class Queue:
  def __init__(self):
    self.queue = Stack()

  def push(self, int):
    self.queue.push(int)

  def pop(self):
    x = self.queue.peek()
    self.queue.remove(x)
    return x

  def peek(self):
    x = self.queue.peek()
    return x
  

  def isEmpty(self):
    if len(self.stack) == 0:
      return True
    return False


queue = Queue()
queue.push(1)
queue.push(1)
queue.push(1)
print(queue.)

input = ["Queue", "push", "push", "peek", "pop", "isEmpty"]
pushval = [[], [1], [2], [], [], []]

# Output [null, null, null, 1, 1, false]

for i in range(len(input)):
  if input[i] == "Queue":
    myqueue = Queue()

  if input[i] == "push":
    myqueue.push(pushval[i])
    
  if input[i] == "pop":
    print(myqueue.pop())
    print(myqueue)
    
  if input[i] == "peek":
    print(myqueue.peek())
    
  if input[i] == "isEmpty":
    print(myqueue.isEmpty)
  
      
  
        





      