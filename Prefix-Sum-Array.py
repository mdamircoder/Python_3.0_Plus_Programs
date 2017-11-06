
def PrefixSum (a): # Prefix Sum Array generator
    PrefSumArray = [ a[0] ]
    n = len(a)
    for i in range(1, n):
        PrefSumArray.append( PrefSumArray[i-1] + a[i] )
    return PrefSumArray
	
# =========================================================================================

a = [ 5, 1, 8, 6, 12, 56, 8, 121 ]
PrefSumArray = PrefixSum( a )
print( "Actual Array :", a )
print( "Prefix Sum Array :", PrefSumArray )

'''============================= S A M P L E     O U T P U T =============================
Actual Array : [5, 1, 8, 6, 12, 56, 8, 121]
Prefix Sum Array : [5, 6, 14, 20, 32, 88, 96, 217]
========================================================================================'''
