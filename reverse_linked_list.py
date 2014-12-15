# stolen from the interwebz

class Node:
  def __init__(self,value,next):
    self.value = value
    self.next = next
 
def prnt(n):
  next = n.next
  print n.value
  if(next is not None):
    prnt(next)
 
#Iterative
def reverse(n):
  previous = None
  current = n
 
  while current is not None:
    next = current.next
    current.next = previous 
    previous = current
    current = next
 
  return previous
 
#Recursive
def recurse(n,previous):
  if n is None:
    return previous
  next = n.next
  n.next = previous
  return recurse(next, n)
 

nD = Node(4,None)
nC = Node(3,nD)
nB = Node(2,nC)
nA = Node(1,nB)

 
#l = reverse(n3)
prnt(nA)
result = recurse(nA, None)
prnt(result)

