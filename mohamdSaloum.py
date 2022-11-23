import pandas as pd
import glob

loc = r'E:\Fourth Year\machine learning\\*.xlsx'
excel_files = glob.glob(loc)

df1 = pd.DataFrame()

for e_file in excel_files:
    df2 = pd.read_excel(e_file)
    df1 = pd.concat([df1,df2], ignore_index=True)
df1.fillna(value="N/A", inplace=True)


df1.to_excel(r'E:\Fourth Year\machine learning\\Fianal.xlsx')
df1.head()

df1 ["name"] = df1["name"].astype("category")
df1.groupby(by="name").sum()

df1.groupby(by="name").count()
