class Joker:
    def __init__(self,name,power,pyscho):              #Subtask 1
        self.name =name
        self.power = power
        self.num_of_wife = 100
        self.is_he_psycho= pyscho


j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')

#Subtask 2
print("The first if/else block prints the output as 'different' because it is checking the locations of two objects upon same class.As we know the location of two objects can never be same thus, it is printing 'different'")

#Subtask 3
print("The second if/else block prints the output as 'same' because the parameter of j1 has been set as 'Health Ledger' initially but at first in j2 the name parameter was been assigned with 'Joaquin Phoenix' and later the value of name in j2 object has been assigned with 'Heath Ledger'.Now j1.name and j2.name contains the similar String input. Thus, despite of having different locations of the two objects j1 and j2 in second if/else block the comparison is done in between of assigned string and because of that the output shows 'same'. ")