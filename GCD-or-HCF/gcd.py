
from math import gcd

gcd_of_12_and_15 = gcd(12, 15)
print( "1. GCD of 12 and 15 is :", gcd_of_12_and_15 )

print( "1. GCD of 15 and 6 is :", gcd(15, 6) )
print( "2. GCD of 5 and 6 is :", gcd(5, 6) )
print( "3. GCD of 0 and 6 is :", gcd(0, 6) )
print( "4. GCD of -4 and 10 is :", gcd(-4, 10) )
print( "5. GCD of 4 and -10 is :", gcd(4, -10) )
print( "6. GCD of -4 and -10 is :", gcd(-4, -10) )

'''#######################################################

gcd(argument_1, argument_2) is an inbuilt method in Python.
** This method takes only two arguments (Integers).
**  You just need to import it from library 'math'.

Remember, gcd(-a, -b) = gcd(-a, b) = gcd(a, -b) = gcd(a, b)

################ S A M P L E   O U T P U T ###############
GCD of 12 and 15 is : 3
1. GCD of 15 and 6 is : 3
2. GCD of 5 and 6 is : 1
3. GCD of 0 and 6 is : 6
4. GCD of -4 and 10 is : 2
5. GCD of 4 and -10 is : 2
6. GCD of -4 and -10 is : 2
#######################################################'''
