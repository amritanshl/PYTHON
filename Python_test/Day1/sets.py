# set
st ={'a', 'b','c','d'}

#length of aset
print(len(st))

#check item
print("I wanted to check a certain item  ", 'c' in st)

if ('c' in st):
    print('c exists in st ')
else:
    print('c does not exists ')

#add anew item
st.add('x')   
print(st)

#remove the item
st.remove('x')
print(st)

#st.clear()

set1 = {'a','b','c','d'}
set2 = {'c','d','g','h'}

#union
#set1.update(set2)
print(set1)


#intersection
print(set1.intersection(set2))
print(set1)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers) )

if(even_numbers.issubset(whole_numbers)):
    print("even number is subset of whole number -- ",even_numbers.issubset(whole_numbers))
else:
    print("it is not ",even_numbers.issubset(whole_numbers))

if(whole_numbers.issuperset(even_numbers)):
    print("whole number is superset of even number -- ",whole_numbers.issuperset(even_numbers))
else:
    print("it is not supersest ",whole_numbers.issuperset(even_numbers))

print(set1.difference(set2))
print(set2.difference(set1))