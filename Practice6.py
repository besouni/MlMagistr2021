import pandas as pd

# path1 = "excel/data1.xlsx"
# cols = ["One", "Two", "Three", "Four"]
# ind=["Row1", "Row2", "Row3"]
# l = [
#         [4, 5, 9, 98],
#         [6, 19, 5, 3],
#         [41, 5, 48, 3]
# ]
# dic = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45],
#   "Pulse":[110, 117, 103]
# }
# print(dic)
# df = pd.DataFrame(dic)
# print(df)
# df.to_excel(path1, index=False, header=False, sheet_name="sheet2", startrow=5, startcol=4)

patch2 = "excel/SampleData.xlsx"
excel = pd.read_excel(patch2, usecols=[1, 2])
# print(excel)
dataList = excel.values.tolist();
print(dataList)
for item in dataList:
    print(item)


