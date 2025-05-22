import numpy as np 
import pandas as pd

a = pd.date_range("20250522",periods=12)
# print(a)

# df = pd.DataFrame({"date":['20250522','20250524','20250526'],"value":[10,20,30]})

# df['date'] = pd.to_datetime(df["date"])  
# df.set_index('date',inplace = True)  
# print(df.resample('D').mean())                                                         
# print(df.resample('D').sum())                                                         
# print(df)
# print(b)
# df = pd.DataFrame({"A":1.0,"B":pd.Timestamp("20250522"),"C":pd.Series(1,index=list(range(4))),"D":np.array([3]*4),"E":pd.Categorical(["test","train","test","train"]),"F":"foo"})
df = pd.DataFrame(np.random.rand(12,4),index = a, columns=list("ABCD"))
# print(df.head())
# print(df.tail())
# print(df.index)
# print(df.columns)
# print(df.to_numpy())
# print(df.describe())
# print(df.T)
# print(df.sort_index(axis=1,ascending=False))
# print(df.sort_values(by='B'))

# Getitem
# print(df['A'])
# print(df[0:3])


# Selection by label
# print(df.loc[a[0]])
# print(df.loc[:,["A","B"]])
# print(df.loc[[a[0]],["A"]])
# print(df.at[a[0],"A"])



# Selection by position
# print(df.iloc[3])
# print(df.iloc[0:3,0:2])
# print(df.iloc[[1, 2, 4], [0, 2]])
# print(df.iloc[1:3, :])
# print(df.iloc[1,1])
# print(df.iat[1,1])



# boolean indexing
# print(df[df['A']>0])
# print(df[df>0])
# df2 = df.copy()
# df2['E'] = range(12)
# print(df2)
# print(df2[df2['E'].isin([2,4])])



# setting
s1 = pd.Series(range(12),index = pd.date_range("20250522",periods = 12))
df['F'] = s1
# print(df)
# df.at[a[0],'A']=0
# df.iat[1,2] = 0
# df.loc[:,'D'] = np.array([5]*len(df))
# print(df)
df2 = df.copy()
df2[df2>0] = -df2
print(df2)