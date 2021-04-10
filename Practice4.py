#==Q_1==
# import random
# def numberOfDigits1(N):
#     sum = 0
#     for digit in str(N):
#         sum += int(digit)
#     return sum
# d={}
# list = random.sample(range(1, 101), 5)
# print(list)
# for x  in list:
#     d[x] = numberOfDigits1(x)
# print(d)
# print(max(d.values()))


#==Q_2==
import random
import statistics
l = []
for i in range(0,20):
    n = random.randint(5, 15)
    l.append(n)
print(l)
print("mode= ",statistics.mode(l))
dic = {}
for i in l:
    dic[i] = l.count(i)
print(dic)


# x = 203
# print(x)
#
# print(x%10)
# x = int(x/10)
# print(x)
#
# print(x%10)
# x = int(x/10)
# print(x)
#
# print(x%10)
# x = int(x/10)
# print(x)
#
#
#
#
#
# def numberOfDigits(N):
#     S = 0
#     while N!=0:
#         S = S+N%10
#         N = int(N/10)
#     return S


# for x in range(1, 100, 10):
#     d[x] = x+x
# print(d)
#
# d1 = {3:87, 'name':"Beso", 'age':37, 7:67}
# print(d1)
# print(d1['name'])
# d1[34]=89
# print(d1)

# 1=2, 11=22, 21=42, 31=62, 41=82, ...
