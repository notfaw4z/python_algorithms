#Checks if the given input is a palindrome or not

def palindrome(word):
    reversed = word[::-1]
    
    if reversed == word:
        return True
    else:
        return False
        

to_check = input("Please enter a value to check for palindrome: ")
print(palindrome(to_check))
