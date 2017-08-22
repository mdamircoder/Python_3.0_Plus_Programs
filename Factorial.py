# Recursive function to find factorial
def fact(n): # recursive manner
    if n==0 : return 1
    else : return n * fact(n-1)

# Block 1
flag = "yes"
while flag.lower() == "yes":
    try:
        n = int(input("Enter the number to find factorial : "))
        print("The factorial of", n, "is", fact(n))
        flag = input("Do you want to find more factorials (yes/no) ? ")
    except Exception as exc:
        print("Error :", exc, ". Try again.")
        flag = "yes"
    print("=======================================================================")

    
# If you want to calculate the factorial for once, use the code below without triple quotes
# keep the function fact()
# Block 2
'''
try:
    n = int(input("Enter the number to find factorial : "))
    print("The factorial of", n, "is", fact(n))
except Exception as exc:
    print("Error :", exc)
'''
