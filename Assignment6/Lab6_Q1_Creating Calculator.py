class Calculator:
    def __init__(self,value1,operator,value2):
        self.value1=value1
        self.operator=operator
        self.value2=value2
    def add (self):
        return self.value1+self.value2
    def subtract (self):
        return self.value1-self.value2
    def multiply (self):
        return self.value1*self.value2
    def divide(self):
        return self.value1/self.value2



x=int(input())
sign=input()
y=int(input())
print("Let's Calculate!")
calculate=Calculator(value1=x,operator=sign,value2=y)
if calculate.operator=="+":
    print("Value 1:",calculate.value1)
    print("Operator:", calculate.operator)
    print("Value 2:", calculate.value2)
    print("Result:", calculate.add())
elif calculate.operator=="-":
    print("Value 1:",calculate.value1)
    print("Operator:", calculate.operator)
    print("Value 2:", calculate.value2)
    print("Result:", calculate.subtract())
elif calculate.operator=="*":
    print("Value 1:",calculate.value1)
    print("Operator:", calculate.operator)
    print("Value 2:", calculate.value2)
    print("Result:", calculate.multiply())
elif calculate.operator=="/":
    print("Value 1:",calculate.value1)
    print("Operator:", calculate.operator)
    print("Value 2:", calculate.value2)
    print("Result:", calculate.divide())


