from mcstatus import JavaServer
import git
import os
from datetime import datetime
import subprocess


#Paste here your git repo
#NOTE: if your repo is in github it will ask for you username and PAT (is not the password), to avoid having to type your credentials, you can use the following:
#https://your-username:your-PAT@github.com/username/repository.git
serverRepo = ""

#Paste here the path to save a clone of the repo
serverPath = ""

#Paste here the IPs of the servers
serverNames = [""]


def canStart(serverIndex):
    try:
        server = JavaServer.lookup(serverNames[serverIndex])
        status = server.status()

        return server, serverNames[serverIndex]
    except:
        if serverIndex < len(serverNames)-1:
            return canStart(serverIndex+1)
        else: return None, None


def pullServer():
    if len(os.listdir(serverPath)) == 0:
        print("You haven\'t cloned the repo")
        git.Repo.clone_from(serverRepo, serverPath)
        print("Cloned the repo to {serverPath}")
    else:
        repo = git.Repo(serverPath)
        repo.remotes.origin.pull()
        print("Pulled the latest updated from the repo")



def pushServer():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Stopped the server at: {current_time}"

    repo = git.Repo(serverPath)
    repo.git.add(A=True)
    repo.index.commit(commit_message)
    repo.remotes.origin.push()

    print("Changes saved")


def startMinecraftServer():
    os.chdir(serverPath)

    command = ["java", "-jar", serverPath+"server.jar"]

    process = subprocess.Popen(command)

    process.wait()
    print("Server stopped")

    print("Trying to save changes to the repo")
    pushServer()



if __name__ == "__main__":
    server, server_name = canStart(0)

    if server is None:
        print("You can start the server")
        pullServer()
        print("Starting server...")
        startMinecraftServer()
    else:
        print(f"The server {server_name} is up with {server.status().players.online} players now")
