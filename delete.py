import view
import json
import os
def delete_project(email):
    view.view_project(email)
    if os.path.getsize("create.txt") != 0 :
        project_name = input("enter project name to delete it : ")
        new_file_content=""
        f = open("create.txt","r")
        for line in f :
            project=json.loads(line)
            if email == project["email"] :
                if project_name == project["project_title"] :
                    line = ""
                    print("deleted successfully")
                new_file_content += line     
            else :
                line = json.dumps(project)
                new_file_content += line + "\n"
        f=open("create.txt","w")
        f.write(new_file_content)
        f.close()
