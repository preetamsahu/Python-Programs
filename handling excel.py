import  pandas as pd
# # mydata={
# #     'subject':['math','english','hindi'],
# #     'marks':[23,45,677]
# # }
# # df=pd.DataFrame(mydata)
# # print(df)
# print("hellow")
# df=pd.DataFrame([['john','12','Btech'],['wicky',12,'BE'],['dhan',45,'MTECH']],index=[1,2,3],columns=['name','age','course'])
# # print(df)
# # print(df.columns)
# # print(df.index)
# # print(df.values)
# # print(df['name'])
# df['dob']=[56,54,45]
# print(df)
# # print(df.reindex([2,1,3]))
# # pf=df.drop([1])
# print(df['age'].sum())
# df=pd.Series([1,2,3,4,5,6,6])
# print(df)
# print(df.count())
# print(df.sum())
# print(df.median())
# print(df.median())
# print(df.mean())
# print(df.std())
# print(df.min())
# print(df.min())
age_list = [['Afghanistan','10/12/202',8425333,'Asia'],
            ['Australia','10/12/202',9712569,'Oceania'],
            ['Brazil','10/12/202',76039390,'Americas'],
            ['China','10/12/202',637408000,'Asia'],
            ['France''10/12/202',44310863,'Europe'],
            ['India','10/12/202',None,'Asia'],
            ['United States','1957',171984000,'Americas'],
            ['India','10/12/202',None,'Asia'],
            ['India','10/12/202',None,'Asia'],
            ['United States','1957',171984000,'Americas'],
            ['United States','1957',171984000,'Americas'],
            ['United States','1957',171984000,'Americas']]
df=pd.DataFrame(age_list,columns=['Country','Year', 'Population','Continent'])
print(df)
print('-------------------------')
# print(df.sort_values('Year',ascending=False))
print('-------------------------')
print(df.sort_index(ascending=False))
print('-------------------------after drop')
print(df.dropna())
print('-------------------------after dropnanana')
df['Year']=pd.to_datetime(df['Year'])
print(df)
# df.drop_duplicates(inplace=True)
# print('-------------------------after dropnanana')
#
# print(df.loc[3,'Country'])
