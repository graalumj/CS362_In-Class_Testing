# Palindrome
# By: Jason Graalum
def palindrome(str):
    if(len(str) < 1):
        return False
    else:
        return str.lower() == str[::-1].lower()

if __name__ == '__main__':
    str = raw_input("Enter a palindrome: ")
    
    if(palindrome(str)):
        print(str + " is a palindrome")
    else:
        print(str + " is not a palindrome")
        
