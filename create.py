import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("WORKSPACEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()

    private = True
    while True:
        isPrivatePrompt = input("Create private repository (y/N):")
        if isPrivatePrompt.startswith("y") or isPrivatePrompt.startswith("Y"):
            private = True
        elif isPrivatePrompt.startswith("n") or isPrivatePrompt.startswith("N") :
            private = False
        else:
            private = None
        
        if private is not None:
            break

    description = input('Project description:')

    repo = user.create_repo(folderName, private=private, description=description)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
