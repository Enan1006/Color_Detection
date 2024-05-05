import numpy as np
# ===========   1   ============
arr_1 = np.array([(1,2,3),(4,5,6)])
print('Array 1', arr_1)

# ===========   2   ============
arr_2 = np.array([(1,2,3)]),([(4,5,6)])
print('Array 2', arr_2)


# ------------  5   --------------
# This method can be used to put Impurities or say Noise in an image
arr_5 = np.random.rand(2, 4) * 255
# this variable will return a matrix of 2*3 with every random value between 0 and 1 multiplying by 255.
# It's called scalar multiplication
print(arr_5)
#
#
# ==========    6   ==============

# This method can be used to create a matrix with numbers between 0 and the value will be put as 1st parameter
arr_6 = np.random.randint(5,size=(2,3))
print("Array 6", arr_6)