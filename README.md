# MultiPCMinecraftServer
A Python tool that aims to help groups of people host a minecraft server between different PC's one at a time

## Dependencies
You will need to have installed Python (obviously), and the following modules:
- GitPython
- mcstatus

Install them using:
```
pip install GitPython mcstatus
```

## What does it do?
This script manages a Minecraft server using a Git repository to store and sync server files. It checks a list of servers to see if any are online to prevent multiple instances from running simultaneously. If no servers are online, it pulls the latest files from the repository, starts the Minecraft server, and after the server stops, it pushes any file changes back to the repository. This ensures server data is always up-to-date and version-controlled.

## Why?
Some friends and I wanted to play some Minecraft with mods but had no money to pay for a host. So we decided to host the server ourselves. The problem started when the person that had the server could play some day, so we had to be moving the files from one computer to another and always checking that no one had started the server previously. One day I decided to try and fix that, and this is my attempt to do so.

## Do I have to change the code?
Yes. But only some variables:
- **serverRepo:** The url of your repository
- **serverPath:** The path where you will be saving the repository and the server files
- **serverNames:** An array to store the IP's of the different PC's that will host the server

## Note about the server repository
If you are planning to use a GitHub repository you will need to generate a PAT (Personal Access Token) for your profile, [here's a link](https://www.geeksforgeeks.org/how-to-generate-personal-access-token-in-github/) that explains how to do so.
Also in the **serverRepo** variable I would use the following value: 
```https://your-username:your-PAT@github.com/username/repository.git```

## Suggestions
Feel free to:
- Open an Issue for suggestions or feature requests.
- Fork the repository and contribute your own improvements.

## If you want to help me buy Elden Ring:
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J018V8XS)
