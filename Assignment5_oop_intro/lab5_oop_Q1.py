class DataType:                                         #Subtask 1
    def __init__(self,name,values):                     #Subtask 2
        self.name=name
        self.values=values


data_type1 = DataType("Integer",1234)
print(data_type1.name)
print(data_type1.values)
print('=====================')
data_type2 = DataType("String","Hello")
print(data_type2.name)
print(data_type2.values)
print('=====================')
data_type3 = DataType("Float",4.0)
print(data_type3.name)
print(data_type3.values)

