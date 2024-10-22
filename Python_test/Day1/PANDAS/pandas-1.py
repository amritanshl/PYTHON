# import pandas as pd

# data1 = pd.DataFrame( {'col1': [1,2,3,4,7,11],'col2': [4,5,6,9,5,0],'col3': [7,5,8,12,1,11]})
# # data2 = {'col1': [1,2,30,4,7,110],'col2': [4,50,6,90,50,0],'col3': [7,50,80,12,10,11]}

# # df = pd.DataFrame(data=data1)
# # df1 = pd.DataFrame(data=data2)
# # # col1 = df.nsmallest(3,'col1')
# # # col2 = df.nsmallest(3,'col2')
# # # col3 = df.nsmallest(3,'col3')

# # # print(col1)
# # # print(col2)

# # # print(col)

# # print(df.ne(df1))
# #df = pd.read_csv('nba.csv')
# #print(df.head(10))
# # df_agg = df.aggregate({"LineTotal":['sum','min','max'],
# #                        "UnitPrice":['sum','min','max']})
# # print(df_agg)
# data1.insert(1,"col4", [5,8,4,6,7,6],True)




# df2 = df.query("tcode =='t2'") 

# print(df2)


# import pandas as pd

# data = pd.read_csv('world_alcohol.csv')
# # print(data.shape)
# # print(data.columns)



# print(data.iloc[1:50:5])
#Write a Pandas program to split the following dataframe into groups based on school code. Also check the type of GroupBy object.
# import pandas as pd
# df = pd.DataFrame({
#     'school_code': ['s001','s002','s003','s001','s002','s004'],
#     'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#     'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#     'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#     'weight': [35, 37, 33, 30, 31, 32],

#     'tcode': ['t1', 't2', 't3', 't4', 't5', 't6']})   
# #df = df.set_index(['school_code','class','tcode','name'])

# df3 = pd.DataFrame({
#     'school_code': ['s001','s002','s003','s001','s002','s004'],
#     'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#     'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#     'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#     'weight': [35, 37, 33, 30, 31, 32],

#     'tcode': ['t1', 't2', 't3', 't4', 't5', 't6']})   
# #df3 = df.set_index(['school_code','class','tcode','name'])

# # df2 = df.groupby(['school_code'])
# # print(type(df2))

# # for x in df2:
# #     print(x)

# combine = pd.concat([df,df3])
# print(combine)


import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'def': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 37, 33, 30, 31, 32],
    'tcode': ['t1', 't2', 't3', 't4', 't5', 't6']})
df.set_index(['def'], inplace=True)
# df.astype(str)
# Select rows by filtering on one or more columns
# filtered_df = df.query("school_code == 's001' and `class` == 'V'")
filtered_df = df.query("weight == 35 and def == 'V' ")
print(filtered_df)