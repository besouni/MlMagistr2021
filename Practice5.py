import numpy as np

# # print(np.__version__)
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 19, 10, 11, 12])
# print(arr1)
# print(arr1[8])
# print("=============")
#
# arr2 = np.array( [  [1, 2, 3, 4, 5, 6],
#                     [7, 8, 19, 10, 11, 12]
#                     ])
# print(arr2)
# print("=============")
# arr3 = np.array( [  [ [1, 2, 3], [4, 5, 6]],
#                     [ [7, 8, 19], [10, 11, 12]]
#                     ])
# print(arr3)
# print("=============")

a1 = np.array([32, 5, 9, -8, 0, 13, 4, 5, 8, 10, -4, 34])
print(a1[0])
print(a1[11])
print("=============")

a2 = np.array([
               [32, 5, 9, -8, 0, 13],
               [4, 5, 8, 10, -4, 34],
               [-4, -5, 18, 1, 7, 24]
            ])

print(a2[0][3])
print(a2[1][2])
print(a2[2][4])

a3 = np.array()


# x=np.random.randint(20, size=(12))
# print(x)

