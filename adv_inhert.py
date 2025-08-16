# #single or basic inheritance

# class Parent:
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# child=Child("Alice")
# child.greet()       
# child.play()


#multi-level inheritance

# class Grandparent:
#     def __init__(self,name):
#         self.name=name

#     def tell_story(self):
#         print(f"{self.name} tells a story")

# class Parent(Grandparent):

#     def work(self):
#         print(f"{self.name} is working")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# child=Child("Bob")
# child.tell_story()
# child.work()    
# child.play()

#hierarchical inheritance

# class Parent:
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is playing")

# child1=Child1("Charlie")
# child2=Child2("Diana")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()


#multiple inheritance
# class A:
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         print(f"Hello from A,{self.name} ")

# class B(A):
#     def greet(self):
#         print(f"hello from B, {self.name}")
#         super().greet()

# class C(A):
#     def greet(self):
#         print(f"hello from C, {self.name}")
#         super().greet()

# class D(B,C):
#     def greet(self):
#         print(f"Hello from D,{self.name}")
#         super().greet()

# d=D("Frank")
# d.greet()


#hybrid
class Animal:
    def __init__(self,name):
        self.name= name
    
    def sound(self):
        print(f"{self.name} makes a sound")

class Mamal(Animal):
    def feeding(self):
        print(f"{self.name} is feeding milk")

class Bird(Animal):
    def flying(self):
        print(f"{self.name} is flying")

class Bat(Mamal,Bird):
    def __init__(self,name):
        Mamal.__init__(self,name)
        
    def noctural(self):
        print(f"{self.name} is noactural")

b=Bat("Bruce")
b.sound()
b.feeding()
b.flying()
b.noctural()