#how do you craete a module from the file rough.py
#name of the file and you import the class from it

#from oops_proj import chatbook
#user1=chatbot()


#function vs method
#function
#list=[1,2,3,4,5]
#a1=len(list)
#print(a1)


#user1=chatbook() #object of the class
#user1.send_message()#here the method is being accessed from the class
#here the method is being called with the help of an object
#method is also a fuction but it is defined inside a class
#print(user1.name)



#getter and setter methods
#print(user1.get_name())
#user1.set_name("Adithi")
#print(user1.get_name())

from oops_proj import chatbook

user1 = chatbook()
print(user1.id)  # 1

chatbook.set_id(10)

user2 = chatbook()
print(user2.id)  # 10

user3 = chatbook()
print(user3.id)  # 11
