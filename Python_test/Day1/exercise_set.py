# # import pandas as pd

# # myDict = {'dict1':['student_id', 1, 'name', 'Jean Castro', 'class', 1000], 
# #           'dict2':['student_id', 2, 'name', 'Lula Powell', 'class', 10000], 
# #           'dict5':['student_id', 5, 'name', 'Zachary Simon', 'class', 'VII']}

# # #for y in zip(*([key]+(value) for key,value in (myDict.items()))):

# #    # print(*y)

# # #df = pd.DataFrame.from_dict(myDict)

# # #print(df)




# # # myList = []









# # #tempList = []

# # # for x in range(len(myDict)):
# # #     rollNo = myDict[x]['student_id']
# # #     name = myDict[x]['name']
# # #     calss = myDict[x]['class']
# # #     myList.append(rollNo)
# # #     myList.append(name)

# # #     myList.append(calss)
# # #     tempList.append(myList)
# # #     myList=[]
    
# # #print(tempList)
    
# # # for y in range(len(myDict)):
# # #     myList.append(list(myDict[y].values()))

# # # print(myList)

# # from collections import Counter
# # mylist= []

# # item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# # df = pd.DataFrame.from_dict(item_list)
# # #print(df)

# # # myDict = {}
# # # for item in item_list:

# # #     print(item)
# # #     if(myDict[item.keys()]):
# # #         myDict[item[0]] += item[1]
# # #     else:
# # #         myDict[item[0]] = item[1]
# # # print(myDict)

# # output = Counter()
# # for x in item_list:
# #     output[x['item']] += x['amount']
# #     print(output[x['item']])
# # #print(output)

# # itemList=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
 
# # myList={}
# # for item in itemList:
# #     if item['item'] not in myList:
# #         myList[item['item']] = item['amount']
# #     else:
# #         myList[item['item']] += item['amount']
# # #print(myList)

 


# dicno= {1:{2:{3:{4:{5:{6:{'Amrit':'firstname'}}}}}}}

# count = 1
# print(dicno.keys())

# while(type(dicno.keys()) is dict):
#     typeOF = type(dicno[count])
#     count = count+1
#     print(typeOF)




# def dict_depth(dic, level = 1):
     
#     if not isinstance(dic, dict) or not dic:
#         return level
#     return max(dict_depth(dic[key], level + 1)
#                                for key in dic)
 
# dic = {1:'a', 2: {3: {4: {}}}}

# # def dict_depth(dic, level = 1):
      
# #     str_dic = str(dic)
# #     counter = 0
# #     for i in str_dic:
# #         if i == "{":
# #             counter += 1
# #     return(counter)
  
# # # Driver code
# # dic = {1:'{Gee{k', 2: {3: {4: {}}}}
# # print(dict_depth(dic))




dict1 = ['S001', 'S002', 'S003', 'S004']
dict2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
dict3 = [85, 98, 89, 92,55]


print([[a,b,c] for (a,b,c) in zip(dict1,dict2,dict3)])
dict3.copy.dee






