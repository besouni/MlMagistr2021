import pandas as pd
import numpy as np
# import scipy.stats as stats
from scipy import stats as st

patch = "data/sampledatafoodsales.xlsx"
excel = pd.read_excel(patch)
# print(excel)
data = excel['Quantity'].tolist()
# print(data)
# print(len(data))
sash_aritmetikuli = np.mean(data)
sash_aritmetikuli  = np.round(sash_aritmetikuli, 0)
print("Mean->{0}".format(sash_aritmetikuli ))
mediana = np.median(data)
print(("Mediana->{0}".format(mediana)))
moda = st.mode(data)
print("Mode->{0}".format(moda))
print("Mode->{0}; count->{1}".format(moda[0][0], moda[1][0]))
print("Max->{0}; Min->{1}; GANI->{2}".format(np.max(data), np.min(data), (np.max(data)-np.min(data))))
std = np.std(data)
print("STD->{0}".format(np.round(std)))
print(data)
procentuluridone50 = np.percentile(data, 50)
print("procentuluridone50->{0}".format(procentuluridone50))
procentuluridone90 = np.percentile(data, 90)
print("procentuluridone50->{0}".format(procentuluridone90))









