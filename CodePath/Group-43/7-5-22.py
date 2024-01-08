class numStack:

  def __init__(self, l):
    self.stack = []
    for i in l: self.push(i)
  
  def push(self, i):
    self.stack.append(i)
  
  def pop(self):
    return self.stack.pop()

    
# def main():

#   s = MinStack([1])
#   print('Test 1:', s.get_min() == 1)
    
# main()
    


def postfix(string):
  stack = []
  val = 0
  
  for token in string:
    if token not in "+-*/":
        stack.append(int(token))
        continue
    
    v2 = stack.pop()
    v1 = stack.pop()
    
    if token =="+":
        val = v1+v2
    elif token == "-":
        val = v1-v2
    elif token == "*":
        val = v1*v2
    else:
        val = int(v1/v2)
    stack.append(val)
  return stack.pop()
    
  # too many numbers not enough operand
  return numStack.pop()
    
string1 = ["2","1","+","3","*"]

print(postfix(string1))
  
        





      