class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True


wadiya = Wadiya()                                            #Subtask 1
print("Part 1:")                                             #Subtask 2
print("Name of President:", wadiya.name)
print("Designation:", wadiya.designation)
print("Number of wife: ", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)


wadiya.name = "Donald Trump"                                   #Subtask 3
wadiya.designation = "President"
wadiya.num_of_wife = 1
wadiya.dictator = "False"
print("Part 2:")
print("Name of President:", wadiya.name)
print("Designation:", wadiya.designation)
print("Number of wife:", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)

if wadiya.name == "Aladeen":                  #checking for name  # #Subtask 4
    print("No, changing had no effect on previous value")
else:
    print("previous information lost")
