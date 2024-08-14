class Stack :
  def __init__(self) :
    self.arr = []

  def push(self, Num) :
    self.arr.append(Num)

  def pop(self) :
    if not self.is_empty() :
      return self.arr.pop()
    return None
  
  def peek(self) :
    if not self.is_empty() :
      return self.arr[-1]
    return None
  
  def is_empty(self) :
    return len(self.arr) == 0

  def __str__(self) :
    return str(self.arr)

stack1 = Stack()
stack1.push(5)
print("Push : ", stack1)
stack1.push(10)
print("Push : ", stack1)
stack1.peek()
print("Peek : ", stack1)
stack1.pop()
print("Pop  : ", stack1)