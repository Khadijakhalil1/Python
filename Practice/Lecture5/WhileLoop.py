num = (1,5,8,3,9,2,6,7)
x = int(input("Enter Num to search :"))
i=0
while i < len(num):
    if(num[i] == x):
     print("Found",i)
    else:
     print("Finding........")
    i+=1
print("Ending")