from datetime import datetime
import json
import re
proj_dic = {}
def create_project(email):
        print("\n Now , you are going to start project\n")
        format = "%Y-%m-%d"

        title=input("please, Enter Your title : ")
        while not title or not title.isalpha() :
            title=input("please, Enter Your title : ")

        details=input("please, Enter Your details : ")
        while not details:
            details=input("please, Enter Your details : ")
            
        
        total_target=input("please, Enter Your total_target : ")
        while not total_target.isdigit():
            total_target=input("total target must be number :")

        start_of_project = input("enter start time for the campaign like YYYY-MM-DD : ")
        while True :
            try:
                datetime.strptime(start_of_project, format)
                break
            except ValueError:
                 start_of_project=input("This is the incorrect date  format. It should be YYYY-MM-DD : ")
        end_of_project = input("enter end time for the campaign like YYYY-MM-DD : ")
        while True :
            try:
              datetime.strptime(end_of_project,format)
              break
            except ValueError:
                start_of_project=input("This is the incorrect date  format. It should be YYYY-MM-DD : ")
        print("project created succefully")
        proj_dic.update(project_title=title,project_details=details,project_target=total_target,start_time=start_of_project,end_time=end_of_project,email=email)
        
        
        f=open("create.txt","a")
        f.write(json.dumps(proj_dic) + '\n')
        f.close()


