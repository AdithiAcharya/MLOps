class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        print("starting the execution of data/attributes")
        self.id=123
        self.salary=50000
        self.designation="Software Engineer"
        print("the data/attributes have been executed")
    
    #defining a method/function
    def  travel(self,destination):
        print("this statement of the method will be printed manually")
        print(f"Employee is travelling to {destination}")
        

#creating an object or instnace of the class
sam=employee()
#print(sam.id)
#print(sam.salary)

sam.travel("New York")#you can ignore  the self