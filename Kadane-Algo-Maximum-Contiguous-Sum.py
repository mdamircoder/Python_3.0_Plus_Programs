
def Contiguous_Subarray_Max_Sum(a):
    size = len(a)
    max_overall = - min(a) - 1 # Initialize by the lowest possible negative number
    max_upto_this = 0
    for i in range(size):
        max_upto_this += a[i]
        if max_overall < max_upto_this :
            max_overall = max_upto_this
        if max_upto_this < 0 : # no need to consider negative contiguous subarrays
            max_upto_this = 0
    return max_overall

a = [ -1, -3, 8, -1, -4, 4, 5, -2 ]
print("Largest Contiguous Sum :", Contiguous_Subarray_Max_Sum(a))

'''========================== S A M P L E     O U T P U T =============================
Largest Contiguous Sum : 12
===================================================================================='''
