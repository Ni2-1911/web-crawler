#create-directory
import os
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project: ' + directory)
        os.mkdir(directory)

directory_name = input('ENTER DIRECTORY NAME HERE:')
create_project_dir(directory_name)

