import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x1 = [2, 4, 6, 8]
y1 = [3, 7, 5, 10]

age = np.random.randint(20, 36, size=(15))
salary = np.random.randint(1000, 5000, size=(15))

# print(age)
# print(salary)
# age = x1
# salary = y1



# print(slope)
# print(intercept)

# def f(x):
#     return x+5
#
# print(f(7))
#
# a = [2, 4, 7]
# print(f(a))
# result = map(f, a)
# print(list(result))

# age = x
# salary = y
slope, intercept, r, p, std_err = stats.linregress(age, salary)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, age))

plt.scatter(age, salary)
plt.plot(age, mymodel)
plt.show()
print(r)

speed = myfunc(14)
# print(speed)
# print(myfunc(1))
print(std_err)
