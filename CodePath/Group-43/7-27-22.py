'''
def reverseWord(arr):
  res = []
  tmp = []
  for i in range(len(arr) - 1, -1, -1):
    if arr[i] == " ":
      tmp.reverse()
      for char in tmp:
        res.append(char)
      res.append(" ")
      print(tmp)
      tmp.clear()
    else:
      tmp.append(arr[i])
  tmp.reverse()    
  for char in tmp:
    res.append(char)
  return res

# also another change i did, that i forgot to mention was changing 0 -> -1 on line 4, to include the first/last letter, since it's exclusive (i think that's the word)

input = ["h","e","l","l","o"," ","w","o","r","l","d"]
print(reverseWord(input))
'''


"""
input = [h i " " o k]
tmpStore = [k o]
result = [k o " " i h]
          ^ ^
          arr[0], arr[1] = arr[1], arr[0]
"""


'''
import queue

class Stack:
    def __init__(self):
        self.myQueue = queue.Queue()

    def push(self, x):
        self.myQueue.put(x)

    def pop(self):
        return self.myQueue.get()

    def top(self):
        value = self.myQueue.get()
        self.myQueue.put(value)  #2,3,4,1
        for i in range(self.myQueue.qsize() - 1):
            self.myQueue.put(self.myQueue.get())
        return value

    def empty(self):
        if (self.myQueue.qsize() == 0):
            return True
        else:
            return False


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.pop())
print(stack.top())
print(stack.empty())
'''
