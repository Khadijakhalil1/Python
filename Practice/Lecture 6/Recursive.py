def convert(dollar):
 pkr=dollar*282.51
 print(dollar,"Dollar Convert into ",pkr,"Pakistani Rupee")
convert(345)
# Recursive Function
def fact(n):
   if(n == 0 or n == 1):
    return 1
   else:
    return fact(n-1)*n
   
print(fact(6))
# print sum by resursion
def sum(n):
  if(n==0):
   return 0
  else:
   return n+sum (n-1)
print("sum of natural num  is",sum(8))