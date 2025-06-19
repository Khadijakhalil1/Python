def check_palindrome(str):
    
    clean_str =(str.replace(" ","")).lower()
    
    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

str = input("Enetr a sting:")
if check_palindrome(str):
    print("it is a palindrome string")
else:
    print("it is not a palindrome string")
