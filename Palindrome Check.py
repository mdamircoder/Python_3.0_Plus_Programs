def PalindromeChecker():
    s = input("Enter a string or number to check Palindrome :")
    if s == s[::-1] : # s[::-1] denotes the reverse string of the string s
        print(s, "is Palindrome.")
    else:
        print(s, "is not Palindrome.")

flag = "yes"
while flag.lower() == "yes" :
    PalindromeChecker()
    flag = input("Do you want to check more (yes/no) ?")
    print("============================================================")


# If you want to check Palindrome for once, use the code given below
# Exclude the triple quotes during use
'''
s = input("Enter a string or number to check Palindrome :")
if s == s[::-1] : # s[::-1] denotes the reverse string of the string s
    print(s, "is Palindrome.")
else:
    print(s, "is not Palindrome.")
'''
