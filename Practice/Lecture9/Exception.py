a = int(input("Enter a: "))
b = int(input("Enter a: "))

try:
    result =a/b
except ZeroDivisionError:
    print("Error: cannot divide by zero")
finally:
    print("Division operation completed: ",result)