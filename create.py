import os 
import subprocess
import sys
import time 
import signal 

frontend_folder_name = None
def create_env():
     env_name = input("Enter ENV name").lower()
     subprocess.run(['cmd','/c','python','-m','venv',env_name])
     print("Environmet Created")

def create_frontend ():
        global frontend_folder_name
        #getting the frontend folder name
        frontend_folder_name = input("Enter the frontend folder name \n")

        #creating frontend using npm vite 
        process = subprocess.Popen(["cmd","/c","npx","-y","create-vite@latest",frontend_folder_name,"--template","react"] , creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        time.sleep(30)
        process.kill()
       

def create_backend():
    backend_dependencies = ['django','djangorestframework','djangorestframework-simplwjwt','django-cors-headers','pillow']
    backend_folder_name = input("Enter the Backend Folder name")
    for dependency in backend_dependencies:
         subprocess.run(["cmd","/c","pip","install",dependency])
    subprocess.run(["cmd","/c","django-admin","startproject",backend_folder_name])

def creat_folders_in_frontend():

    frontend_dir = os.path.join(os.getcwd(),"frontend")
    cur_dir = os.getcwd()

    if os.path.basename(cur_dir) == "frontend":
        print("Already inside the frontend folder")
    else:
        if os.path.exists(frontend_dir):
            os.chdir(frontend_dir)
        else:
            print("Frontend folder doesn't exist")
            return

    folders = []
    files_map = {}

    while True:
        page = input("Enter name of the page (type done to close): ").lower()

        if page == "done":
            break

        folders.append(page)
        files = []

        while True:
            file = input(f"Enter file name for {page} (type done to exit): ").lower()

            if file == "done":
                break

            files.append(file)

        files_map[page] = files

    sub_folders = ["css","jsx"]

    for folder in folders:

        os.makedirs(folder, exist_ok=True)

        for sub in sub_folders:

            sub_path = os.path.join(folder, sub)
            os.makedirs(sub_path, exist_ok=True)

            if folder in files_map:

                for file in files_map[folder]:

                    if sub == "css":

                        css_path = os.path.join(sub_path, f"{file}.css")

                        if not os.path.exists(css_path):
                            open(css_path,"w").close()

                    elif sub == "jsx":

                        jsx_path = os.path.join(sub_path, f"{file}.jsx")

                        component_name = file.capitalize()

                        boilerplate = f"""import React from "react";
import "../css/{file}.css";

export const {component_name} = () => {{
  return (
    <div className="{file}">
      <h1>{component_name} Page</h1>
    </div>
  );
}};
"""

                        with open(jsx_path,"w") as f:
                            f.write(boilerplate)

    print("Frontend structure created successfully")
user_input = input("Select what you want to create ? \n 1. Frontend \n 2. Backend \n 3. Folders in frontend \n 4. Create Environment \n")

if user_input == "1":
    create_frontend()
elif user_input =="2":
     create_backend()
elif user_input == "3":
    creat_folders_in_frontend()
elif user_input == "4":
     create_env()
else :
     print("Wrong input ")