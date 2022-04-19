import json
import os
def view_project(email):
    if os.path.getsize("create.txt") != 0 :
        count=1
        f = open("create.txt","r")
        for line in f :
            project=json.loads(line)
            if email == project["email"] :
                print(str(count) +") "+ project["project_title"])
                count += 1
        f.close()
        if count == 1:
            print(" there is no projects ")
    else :
        print("there is no projects ")


  
