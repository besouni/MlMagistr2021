# ==="Exercise 2_6===
import os
print("Exercise 2_6")
if not os.path.exists("myFiles"):
    os.mkdir("myFiles")
f = open("myFiles/data1.txt", "w")
l = [*range(0, 101)]
# l1 = []
# for el in range(0, 101):
#     l1.append(el)
# print(l1)
# print(l)
# f.write(str(l))
s = ', '.join(str(item) for item in l)
# print(s)
f.write(s)
f.close()