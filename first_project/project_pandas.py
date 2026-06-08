import pandas as pd
import numpy as np
dict = {"Apple":[30],
        "Banana": [21]}
df = pd.DataFrame(dict)
print(df)
dict = {"Apple":[45],
        "Banan":[55]}
df = pd.DataFrame(dict, index = ["2017 Sales", "2018 Sales"])
print(df)
ingredient = {"Flour":["4 cups"],
              "Milk":["1 cup"],
              "Eggs":["2 large"],
              "Spam":["1 can"]}
ingredient = {"Ingredient":["Flour", "Milk", "Eggs", "Spam"],
              "Amount":["4 cups", "1 cup","2 large","1 cam"]
    
}
df = pd.DataFrame(ingredient,)
# print(df)
print(df["Amount"])
df = pd.read_csv("data.csv")
print(df.info)
d = { "First Score":[100, 90, np.nan, np.nan],
     "Second Score":[30,45,np.nan,np.nan],
     "Thrird Score":[np.nan,np.nan,50,98]}
df = pd.DataFrame(d)
print(df)
# mv = df.isnull
df.dropna(inplace = True)
print(df)
# print(mv.sum())
data = {"Name":["Anna", "Levon","Karen","Sona","Armen","Ani"],
        "Experience":[5, 2, 4, 1, 6, np.nan],
        'Performance_Score': [85, 90, 75, 95, 60, 88],
        'Department': ['IT', 'IT', 'HR', 'Finance', 'HR', 'IT']}
df = pd.DataFrame(data)
# print(df)
filtering_df = df[(df['Experience'] > 3) & (df["Performance_Score"] >= 80)]
mean_df = df["Experience"].mean()
df["Experience"] = df["Experience"].fillna(mean_df)
df["New_column"] = df["Performance_Score"] / df["Experience"]
print(df)
print(mean_df)
print(df_experience)
print(df)
print(filtering_df)
group_df = df.groupby("Department")["Performance_Score"].mean()
print(group_df)
sorted_df = df.sort_values(by = "Performance_Score")
print(df)

phones_data = {'Phone_Model': ['iPhone 15', 'Galaxy S24', 'Pixel 8', 'Xiaomi 14', 'OnePlus 12', 'iPhone 14', 'Galaxy S23'],
    'Brand': ['Apple', 'Samsung', 'Google', 'Xiaomi', 'OnePlus', 'Apple', 'Samsung'],
    'Price_USD': [999, 899, 699, np.nan, 799, 799, 699],
    'Rating': [92, 90, 85, 88, np.nan, 84, 86],
    'Units_Sold': [1500, 1200, 800, 950, 600, 1100, 900]
}
df = pd.DataFrame(phones_data)

mean_price = df["Price_USD"].mean()
print(df)
df["Price_USD"] = df["Price_USD"].fillna(mean_price)
df["Rating"] = df["Rating"].fillna(85)
df["Total_Revenue"] = df["Price_USD"] * df["Units_Sold"]
good_deals_df = df[(df["Rating"] > 85) & (df["Price_USD"] < 900)]
print(df)
sorted_phonesdf = df.sort_values(by = "Price_USD", ascending=False)
# print("Thi is sorted " ,sorted_phonesdf)
group_df = df.groupby("Brand")["Units_Sold"].sum()
print(group_df)
print(mean_price)
brand_sumery = df.pivot_table(
     index  = "Brand",
    values = ["Price_USD",'Units_Sold'],
    affgunc= {"Price_USD":'mean', 'Units_Sold':'sum'})
print(brand_sumery)
brand_summary = df.pivot_table(
    index='Brand', 
    values=['Price_USD', 'Units_Sold'], 
    aggfunc={'Price_USD': 'mean', 'Units_Sold': 'sum'}
)
print("--- Բրենդների Ամփոփ Պրոֆիլ ---")
print(brand_summary)
def categorize_price(price):
    if price > 90:
        return 'premium'
    elif price >= 700:
        return "mid_rande"
    else:
        return 'Budget'



        
    


