import view
import json
import os
def edit_project(email):
    view.view_project(email)
    if os.path.getsize("create.txt") != 0 :
        project_name=input("enter project name to edit it : ")
        new_file_content=""
        f=open("create.txt","r")
        for line in f:
            project=json.loads(line)
            if email == project["email"] :
                if project_name == project["project_title"] :
                    count=1
                    print ('\n'+" information of project")
                    for key in project :
                        print(str(count) + ")" + key + " = " + project[key])
                        count += 1
                    print("6) Save ")
                    while True :
                        option=int(input('\n'+"choose the number of value you want to edit : "))
                        if option == 1 :
                            project_title=input('\n'+"enter the new project title :")
                            project.update(project_title=project_title)
                        elif option == 2 :
                            project_details = input('\n'+"enter the new project details : ")
                            project.update(project_details=details)
                        elif option == 3 :
                            project_target = input('\n'+"enter the new project target : ")
                            project.update(project_target=project_target)
                        elif option == 4 :
                            project_start = input('\n'+"enter the new start time for project : ")
                            project.update(start_time=project_start)
                        elif option == 5 :
                            project_end = input('\n'+"enter the new end time for project : ")
                            project.update(end_time=project_end)
                        elif option == 6 :
                            break
                line = json.dumps(project)
                new_file_content += line +"\n"
            else :
                line = json.dumps(project)
                new_file_content += line + "\n"
        fe=open("create.txt","w")
        fe.write(new_file_content)          
        f.close()
