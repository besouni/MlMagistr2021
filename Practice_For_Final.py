import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

count = 100
idNumber1 = random.sample(range(100000000, 999999999), count)
# idNumber2 = random.sample(range(10, 99), count)
idNumber2 = np.random.randint(10, 99, size=(count));
# print(idNumber1)
# print(idNumber2)
def idNumberF(id1, id2):
    return str(id1)+str(id2)
idNumber = list(map(idNumberF, idNumber1, idNumber2))
# print(idNumber)
day1 = np.random.randint(0, 900, count) / 100
day2 = np.random.randint(0, 900, count) / 100
day3 = np.random.randint(0, 900, count) / 100
day4 = np.random.randint(0, 900, count) / 100
day5 = np.random.randint(0, 900, count) / 100
workQuality = np.random.randint(0, 500, count) / 100
data = {
    'id':idNumber,
    'day1': day1,
    'day2': day2,
    'day3': day3,
    'day4': day4,
    'day5': day5,
    'workQuality':workQuality
}

# print(data)

# for key, value in data.items() :
#     print (key, value)

path = "excel/dataForFinal.xlsx"
df = pd.DataFrame(data)
df.to_excel(path, index=False, header=True, sheet_name="data")

excel = pd.read_excel(path, usecols=[1, 2, 3, 4, 5, 6])
# print(excel)
dataList = excel.values.tolist();
fullTimeOfWeek = []
for item in dataList:
    # print(item)
    fullTimeOfWeek.append(round(sum(item[:5]), 2))
workQuality = list(excel["workQuality"])
# print(fullTimeOfWeek)
# print(workQuality)
coWorkers = list(range(1, count+1))
# print(coWorkers)
plt.bar(coWorkers, fullTimeOfWeek)
plt.show()

plt.bar(coWorkers, workQuality)
plt.show()

plt.scatter(fullTimeOfWeek, workQuality)
plt.show()

print("Time Mean={0}".format(round(np.mean(fullTimeOfWeek), 2)))
print("Quality Mean={0}".format(round(np.mean(workQuality), 2)))
print("Time STD={0}".format(round(np.std(fullTimeOfWeek), 2)))
print("50%={0}".format(round(np.percentile(fullTimeOfWeek, 50), 2)))


slope, intercept, r, p, std_err = stats.linregress(fullTimeOfWeek, workQuality)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, fullTimeOfWeek))

plt.scatter(fullTimeOfWeek, workQuality)
plt.plot(fullTimeOfWeek, mymodel)
plt.show()
print("Corellation={0}".format(r))

