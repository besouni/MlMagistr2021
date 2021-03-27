# ==="Exercise 3_4===
import os
print("Exercise 3_4")
if not os.path.exists("myFiles2"):
    os.mkdir("myFiles2")
for i in range(1, 31):
    f = open("myFiles2/data"+str(i)+".txt", "w")
    f.write("Programmer"+str(i))
    f.close()

# ==="Exercise 3_2===
# import os
# print("Exercise 3_2")
# if not os.path.exists("myFiles"):
#     os.mkdir("myFiles")
# f = open("myFiles/data1.txt", "w")
# l = [*range(0, 101)]
# l1 = []
# for el in range(0, 101):
#     l1.append(el)
# print(l1)
# print(l)
# f.write(str(l))
# s = ', '.join(str(item) for item in l)
# print(s)
# f.write(s)
# f.close()