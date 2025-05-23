import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# a = pd.date_range("20250522",periods=12)
# print(a)

# df = pd.DataFrame({"date":['20250522','20250524','20250526'],"value":[10,20,30]})

# df['date'] = pd.to_datetime(df["date"])  
# df.set_index('date',inplace = True)  
# print(df.resample('D').mean())                                                         
# print(df.resample('D').sum())                                                         
# print(df)
# print(b)
# df = pd.DataFrame({"A":1.0,"B":pd.Timestamp("20250522"),"C":pd.Series(1,index=list(range(4))),"D":np.array([3]*4),"E":pd.Categorical(["test","train","test","train"]),"F":"foo"})
# df = pd.DataFrame(np.random.rand(12,4),index = a, columns=list("ABCD"))
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
# s1 = pd.Series(range(12),index = pd.date_range("20250522",periods = 12))
# df['F'] = s1
# print(df)
# df.at[a[0],'A']=0
# df.iat[1,2] = 0
# df.loc[:,'D'] = np.array([5]*len(df))
# print(df)
# df2 = df.copy()
# df2[df2>0] = -df2
# print(df2)


# missing data
# df1 = df.reindex(index=a[0:4],columns=list(df.columns)+['E'])
# df1.loc[a[0]:a[1],'E'] = 1
# print(df1)
# print(df1.dropna(how="any"))
# print(df1.fillna(value=5))
# print(pd.isna(df1))



# operations : Stats
# print(df.mean()) #Calculate the mean value for each column
# print(df.mean(axis=1))#calculate the mean value of each row
# s = pd.Series([1,3,5,np.nan,6,8,9,10,np.nan,np.nan,np.nan,7],index=a).shift(2)#shift(x) shifts values from x places
# print(s)
# print(df.sub(s,axis="index"))



#operations :User defined functions
# print(df.agg(lambda x: np.mean(x)*5.6))
# print(df.transform(lambda x: x * 101.2))



#opeartions : value counts
# s = pd.Series(np.random.randint(0, 7, size=10))
# print(s)
# print(s.value_counts())



#Merge : Conacat
# df =  pd.DataFrame(np.random.randn(10, 4))
# print(df)
# pieces = [df[:3],df[3:7],df[7:]]
# print(pd.concat(pieces))


#Merge : Join
# left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
# right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
# print(left)
# print(right)
# print(pd.merge(left,right,on="key"))

#merge() on unique keys:
# left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
# right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
# print(pd.merge(left, right, on="key"))



#grouping
# df = pd.DataFrame(
#     {
#         "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
#         "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
#         "C": np.random.randn(8),
#         "D": np.random.randn(8),
#     }
# )
# print(df)
# print(df.groupby("A")[["C","D"]].sum())
# print(df.groupby(["A","B"]).sum())



#plotting
# plt.close("all")
# ts = pd.Series(np.random.randn(1000),index = pd.date_range("20250101",periods=1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# df = pd.DataFrame(
#     np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
# )
# df = df.cumsum()
# plt.figure()
# df.plot()
# plt.legend(loc='best')
# plt.show()