class chatbook:

    __user_id=0

    def  __init__(self):
        self.id=chatbook.__user_id
        chatbook.__user_id+=1
        self.__name="Default User"
        self.username=''
        self.password=''
        self.logged_in=False
        #self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id=val

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name=value

    def menu(self):
        user_input=input("""Welcome to chatbook !! how woulf you like me to proceed ?
        1.Press 1 to signup
        2.Press 2  to signin
        3.Press 3 to write a post
        4.Press 4 to message a friend
        5.Press any other key to exit
                         
        -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.send_message()
        else:
            exit()

    #creating a method that will be passed inside the menu method
    def signup(self):
        email=input("Enter your email: ")
        pwd =input("Setup your password: ")
        self.username=email
        self.password=pwd
        print("You have successfully signed up!")
        print("\n")#printing a new line for better readability
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressinf 1 in the main menu")
        else:
            uname=input("Enter your email/username: ")
            pwd=input("Enter your password: ")
            if self.username==uname and self.password==pwd:
                print("You have successfully signed in!")
                self.logged_in=True
            else:
                print("Please input correct credentials...")
        print("\n")
        self.menu()

    def write_post(self):
        if self.logged_in==True:
            txt=input("Enter your message here:")
            print(f"Followingcontent has been posted->{txt}")
        else:
            print("Please sign in first to write a post")
        print("\n")
        self.menu()

    def send_message(self):
        if self.logged_in==True:
            txt=input("Enter your message here->")
            frnd=input("Whom to send to msg? ->")
            print(f"Your message has been sent to {frnd}")
        else:
            print("Please sign in first to send a message")
        print("\n") 
        self.menu()

#creating an instance of the chatbot class  
user1=chatbook()

