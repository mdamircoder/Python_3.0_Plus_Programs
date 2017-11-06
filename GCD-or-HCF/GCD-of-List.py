
from math import gcd # don't forget to import

def gcd_list(arr):
    GCD = arr[0]
    for i in range( 1, len(arr) ):
        GCD = gcd( GCD, arr[i] )
    return GCD

arr = [ 18, 36, 12, 6, -9 ]
result = gcd_list(arr)
print( "GCD for the elements of the list :", result )

'''#######################################################

You can find gcd of more than two numbers stored in a list.
**  Don't Forget 'from math import gcd'
Remember, gcd(-a, -b) = gcd(-a, b) = gcd(a, -b) = gcd(a, b)

################ S A M P L E   O U T P U T ###############
GCD for the elements of the list : 3
#######################################################'''
