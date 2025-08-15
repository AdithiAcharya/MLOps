# #simple inheritance example
# #create a class and add 2 methods, name and speak

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# class Dog(Animal):
#     def __init__(self):
#         self.behavior = "friendly"

#     def speak(self):
#         print(f"Buddy is {self.behavior} and barks")

# dog = Dog()
# dog.speak()

# #call the methods using the object
# #animal=Animal("Generic Animal")
# #animal.speak()

#this is the use of super() keyword
class Animal:
    def __init__(self):
        self.name="Buddy"
    
    def speak(self):
        print(f"{self.name} barks")


class Dog(Animal):

    def __init__(self,breed):
        super().__init__()
        self.breed=breed

    def speak(self):
        super().speak()
        print(f"{self.name} is a {self.breed}")

dog=Dog("Golden Retriever")
dog.speak()