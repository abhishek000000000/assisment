# -*- coding: utf-8 -*-
"""DSA Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V85qXm2S6LU6DfHcVkENxr3Z7nWy7cj3
"""

#PROBLEM FOR ASSIGNMENT :- LINEAR DATA STRUCTURES.
# 1 PROBLEM:- WRITE A PROGRAM TO FIND ALL PAIRS OF AN INTEGER ARRAY WHOSE SUM IS EQUAL TO GIVEN NUMBER.
def print_pairs(arr,n,sum):
  for i in range (0,n):
    for j in range(i+1,n):
      if (arr[i]+arr[j] ==sum):
        print(arr[i],arr[j])
  return ""       
arr=[1,2,3,4,5,6,7,8,9]
n =len(arr)
sum=9
print(print_pairs(arr,n,sum))

# PROBLEM 2:-WRITE A PROGRAM TO REVERSE AN ARRAY IN PLACE? IN PLACE MEANS YOU CANNOT CREATE NEW ARRAY YOU HAVE TO UPDATE ORIGINAL ARRAY

def reverse():
  array=[1,2,3,4,5,6,7,8]
  print("Before Reversing List is: ",array)
  array.reverse()
  print("After Reversing List is: ",array)
  return " "
print(reverse())

# PROBLEM 3: WRITE A PROGRAM TO CHECK IF TWO STRINGS ARE A ROTATION OF EACH OTHER.

def rotation(s1,s2):
  if len(s1) !=len(s2):
    return False
  s3=s1+s1
  if s2 in s3:
    return True
  else:
    return False
s1="helloworld"
s2="worldhello"
rotation(s1,s2)

# PROBLEM 4: WRITE A PYTHON PROGRAM TO PRINT THE FIRST NON-REPEATED CHARACTER FROM A STRING.

def Non_repeating(str):
  dict={}
  size=len(str)
  for i in range(size):
    key=str[i]
    if key not in dict:
      dict[key]=1
    else:
      dict[key]=dict[key]+1
  for key,value in dict.items():
    if(value==1):
      print(key)
      break
  return " "
print(Non_repeating("abcdabcdv"))

#PROBLEM 5: READ ABOUT THE TOWER OF HANOI ALGORITHM.WRITE A PROGRAM TO IMPLEMENT IT.

def TOH(numbers,start,aux,end):
  if numbers==1:
    print("Move disk 1 from road {} to rod {}".format(start,end))
    return
  TOH(numbers-1,start,end,aux)
  print("Move disk {} from rod {} to rod {}".format(numbers,start,end))
  TOH(numbers-1,aux,start,end)
disc=3
TOH(disc,"A","B","C")

#PROBLEM 6: READ ABOUT INFIX,PREFIX AND POSTFIX EXPRESSIONS. WRITE A PROGRAM TO CONVERT POSTFIX TO PREFIX EXPRESSION.

def isOperator(x):
  if x == "+":
    return True
  if x == "-":
    return True
  if x == "/":
    return True
  if x == "*":
    return True
  return False

def post_To_pre(post_exp):
  s = []
  length = len(post_exp)
  for i in range(length):
    if (isOperator(post_exp[i])):
      op1 = s[-1]
      s.pop()
      op2 = s[-1]
      s.pop()
      temp = post_exp[i] + op2 + op1
      s.append(temp)
    else:
      s.append(post_exp[i])

  ans = " "
  for i in s:
    ans += i
  return ans

if __name__ =="__main__":
  post_exp = "AB+cd-"
  print("prefix: ", post_To_pre(post_exp))

# PROBLEM 7: WRITE A PROGRAM TO COVERT PREFIX EXPRESSION TO INFIX EXPRESSION

def prefix_to_infix(prefix):
  stack = []
  i = len(prefix) - 1
  while i >= 0:
    if not isOperator(prefix[i]):
      stack.append(prefix[i])
      i -= 1
    else:
      str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
      stack.append(str)
      i -= 1
  return stack.pop()
def isOperator(c):
  if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c =="(" or c == ")":
    return True
  else:
    return False

if __name__ =="__main__":
  str = "*-A/BC-/AKL"
  print(prefix_to_infix(str))

# PROBLEM 8: WRITE A PROGRAM TO CHECK IF ALL THE BRACKETS ARE CLOSED IN A GIVEN CODE SNIPPET.

def isbalance(expr):
  stack = []
  for char in expr:
    if char in ["(","{","["]:
      stack.append(char)
    else:
      if not stack:
        return False
      current_char=stack.pop()
      if current_char =="(":
        if char != ")":
          return False
      if current_char =="{":
        if char != "}":
          return False
      if current_char =="[":
        if char != "]":
          return False

  if stack:
     return False
  else:
      return True
expr="{()}[]"
print("All Brackets are closed")
isbalance(expr)

# PROBLEM 9 : WRITE A PROGRAM TO REVERSE A STACK

class Stack(object):
  def __init__(self):
    self.items = []
  def push(self,item):
    self.items.append(item)
  def pop(self):
    if self.items ==[]:
      return None
    else:
      return self.items.pop()
  def size(self):
    return len(self.items)
  def isempty(self):
    return self.items ==[]


def reverse(str):
  temstr = " "
  stack = Stack()
  for i in range(len(str)):
    stack.push(str[i])

  while not stack.isempty():
    tem = stack.pop()
    temstr =temstr + tem 

  return temstr
if __name__== "__main__":
  print(reverse("vishal"))

# PROBLEM 10 : WRITE A PROGRAM TO FIND THE SMALLEST NUMBER USING A STACK

my_stack = [1,23,40,677,80,90]
minimum = my_stack[5]
for i in range(len(my_stack)):
  if my_stack[i]< minimum:
    minimum = my_stack[i]

print("Smallest Number in my stack is: ", minimum)