def Max_Prime_Divisor(n):
    
    PrDiv = -1

    if n == 1 : return "N.A." # 1 is handled separately
    
    # All primes are odd numbers except 2
    # We will first check for 2
    # Then for other odd numbers after 3, same procedure
    
    while n % 2 == 0:
        PrDiv = 2
        n = n//2
        
    upto = int(n**0.5) + 1 # math.sqrt(n) + 1
    for odd in range( 3, upto, 2 ):
        while n % odd == 0:
            # Make sure no multiples of prime, enters here
            PrDiv = odd
            n = n//odd

    PrDiv = max (n, PrDiv) # When n is prime itself
    
    return PrDiv

#============================  INPUT SECTION  ============================ 

n = 1564
print("Maximum prime divisor of", n, "is", Max_Prime_Divisor(n)) #23

n = 15
print("Maximum prime divisor of", n, "is", Max_Prime_Divisor(n)) #5

n = 89
print("Maximum prime divisor of", n, "is", Max_Prime_Divisor(n)) #N.A.
n = 1
print("Maximum prime divisor of", n, "is", Max_Prime_Divisor(n)) #-1

n = 25698751364526
print("Maximum prime divisor of", n, "is", Max_Prime_Divisor(n)) #328513
