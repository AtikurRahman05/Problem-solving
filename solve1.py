
# Problem-solving
class User:
    name = ''
    email=''
    password=''
    login = False

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    def login(self):
        email = input("Enter email: ")
        password = input("Enter passward: ")

        if email == self.email and password ==self.password:
            login = True
            print("Login Successfull")
        else:
                print("Login Fail")
    def logout(self):
        login = False
        print("Logged out")
    def isloggedin(self):
        if self.login:
            return True
        else: 
            return False
    def profle(self):
      if self.isloggedin():
        print (self.name,"\n",self.email)
      else:
          print ("User is not logged in")
User= User("Atikur","atikurra00005@gmail.com","12345") 
User.login()
#User = input() 
