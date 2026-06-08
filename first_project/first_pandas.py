import pandas as pd
# import numpy as np

# s = pd.Series(["f","c","e",'4'])
# print( s)
# data = np.array(['g', 'e','k','s'])
# s = ['g', 'e','k','s']
# print(data)

# a = pd.Series(data)
# print("Pandas Series:\n", a)
# list = ["Gor","nare"]
# df = pd.DataFrame(list)
# print("This is a dataframe  " ,df)

# a = pd.Series(list)
# print("this is a series" , a)
# import pandas as pd

# names = ["Gor", "Nare"]

# # DataFrame
# df = pd.DataFrame(names, columns=["Անուն"])

# # Series
# s = pd.Series(names, name="Անուն")


# print("📋 DataFrame:")
# print("=" * 30)
# print(df)

# print("=" * 30)
# print("📌 Series:")
# print("=" * 30)
# print(s)

 
# data = {'Name':['Tom', 'nick', 'krish', 'jack'],
#         'Age':[20, 21, 19, 18]}
# print(data)
 
# df = pd.DataFrame(data)
 
# print(df)
# data = {"Name":['Jai', "Princi", "Gaurav", 'Anuj'],
#         "Age":[27, 24, 22, 32],
#         "Address":['Delhi', 'Kanpur', 'Allahabad', 'Kannuaj'],
#         "Qualific":['Msc','MA','MCA', "Phd"]}
# df = pd.DataFrame(data, index = '22')
# df[["Name", 'Qualific']]
# print(df[df.columns[1:4]])
# print(df.loc[1:3, ['Name']])
# data = {"calories":[420 ,120, 140],
#         "duarition": [ 50,45,60]}
# df = pd.DataFrame(data, index = ['day1', 'day2','day3'])
# print(df.loc["day2"])
df = pd.read_csv("data.csv")
print(df.to_string())
print(df.head())
print(df.tail())
print(df.info())