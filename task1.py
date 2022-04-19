import re 
import json
import sys
import create
import edit
import view
import delete
import sys
from getpass import getpass
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
password_regular_exp =r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'


user_input = {}
def register():

        print("\n Now , you are going to register\n")
    #user_input = {}
        first_name=input("please, Enter Your first name : ")
        while not first_name or first_name.isdigit():
            first_name=input("please, Enter Your first name : ")

        last_name=input("please, Enter Your last name : ")
        while not last_name or last_name.isdigit():
            last_name=input("please, Enter Your last name : ")

        email = input("enter your email : ")
        f = open("users.txt","r")
        for line in f :
            user=json.loads(line)
            while not (re.fullmatch(regex, email)) or email == user["email"]:
                email = input("this email  invalid , try another email : ")

        
        password = getpass("enter your password : ")
        while not password or not (re.fullmatch(password_regular_exp,password)):
            password = getpass("password must be at least 8 characters, at least one letter and one number :")
        confirm_password = getpass("confirm your password : ")
        while confirm_password != password :
            confirm_password=getpass("not match with password , try again : ")
        
        
        mobile_number = input("enter your mobile number : ")
        while not mobile_number.isdigit() :
            mobile_number = input("mobile  should be only numbers : ")

        print (" success registeration ")

        user_input.update(first_name=first_name,last_name=last_name,email=email,password=password,phone=mobile_number)
            
        f=open("users.txt","a")
        f.write(json.dumps(user_input) + '\n')
        f.close()
        check_option()
    
def login():
   
    print("Now , you are going to login\n")
    email = input("please, Enter valid email : ")
    password = input("please, Enter valid password : ")
    f=open("users.txt")
    for line in f :
        user=json.loads(line)
        if email == user["email"] :
            while password != user["password"] :
                password = getpass("your password is incorrect : ")
            print("logged successfully")
            while True:
                check_crud(email)
    else :
        pass
        email = input("please, Enter valid email : ")
    f.close()
       
    
def check_crud(email):
    
    crud=int(input("hello: for create press 1  for view press 2 for edit press 3: for delete press 4: for exit press 5 for exit press 6 \n"))
    if crud == 1:
        create.create_project(email)
    elif crud == 2:
        view.view_project(email)
    elif crud == 3:
        edit.edit_project(email)
    elif crud == 4:
        delete.delete_project(email)
    elif crud == 5:
        sys.exit()
    elif crud == 6:
        from search import search_project
        search_project()
        
    

def check_option():
    option=int(input("hello: for Registration press 1 for Login press 2 for Exit press 3:"))
    if option==1:
        register()
    elif option==2:
        login()
    elif option==3:
        sys.exit()
    else:
        print("plz select number from 1 or 2")
check_option()

