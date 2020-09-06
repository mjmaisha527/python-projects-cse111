class Customer:
    def __init__(self,name):
        self.name=name

    def greet(self,arg=None):

        if arg==None:
            print("Hello!")
        else:
            print("Hello",arg,"!")
    def purchase(self,*items):
        count=len(items)
        print(self.name, "you have purchased", count,"item(s):")

        for x in items:
            print(x)



customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")




















