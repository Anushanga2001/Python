# In here we will get the method
# This methods are already declared in python
List = ['anu', 123, 'Kaluarachchi', 45, 'Anujaya', 36, 'Chathura']	

# get the type of the object
print(type(List))

# get the index
List1 = List.index('Anujaya') 
print(List1)

# replace value
List.append('AJ')
print(List)

# capitalize the list data
# In here first latter will be capital
List[0] = List[0].capitalize()
print(List)

# replace letters
List[0] = List[0].replace('A', 'TJ')
print(List)