import sys
import os
from github import Github

token = "fake_token" #Insert your github token here

def createFlutterProject():
    os.chdir('F:/')
    folderName = str(sys.argv[2])
    os.system('flutter create --org co.shivamgoyal --androidx {}'.format(folderName.lower()))
    os.system('ren {} {}'.format(folderName.lower(), folderName))
    os.chdir(folderName)
    user = Github(token).get_user()
    repo = user.create_repo(folderName, private=True)
    os.system('git init')
    os.system('git add README.md')
    os.system('git commit -m "Project Initialized"')
    os.system('git remote add origin https://github.com/ShivamGoyal1899/{}.git'.format(folderName))
    os.system('git push -u origin master')
    print("\n\n\n\n\n---------- Successfully SetUp {}.\n---------- Remote repository: https://github.com/ShivamGoyal1899/{}\n---------- Local repository: F:/{}\n\n\n\n\n".format(folderName, folderName, folderName))
    os.system('explorer .')

if __name__ == "__main__":
    projectLanguage = str(sys.argv[1])
    if projectLanguage == 'flutter':
        createFlutterProject()