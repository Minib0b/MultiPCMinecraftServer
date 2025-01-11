# MultiPCMinecraftServer
A Python tool that helps groups of people host a minecraft server between different PC's one at a time

## Dependencies
You will need to have installed Python (obviously), and the following libraries:
- GitPython
- mcstatus

## What does it do?
This script manages a Minecraft server using a Git repository to store and sync server files. It checks a list of servers to see if any are online to prevent multiple instances from running simultaneously. If no servers are online, it pulls the latest files from the repository, starts the Minecraft server, and after the server stops, it pushes any file changes back to the repository. This ensures server data is always up-to-date and version-controlled.

## Why?
Some friends and I wanted to play some Minecraft with mods but had no money to pay for a host. So we decided to host the server ourselves. The problem started when the person that had the server could play some day, so we had to be moving the files from one computer to another and always checking that no one had started the server previously. One day I decided to try and fix that, and this is my attempt to do so.

## Do I have to change the code?
Yes. But only some variables:
- **serverRepo:** The url of your repository
- **serverPath:** The path where you will be saving the repository and the server files
- **serverNames:** An array to store the IP's of the different PC's that will host the server

## Suggestions
If you have any suggestions, please create an Issue and I will try to implement it. Or you could fork it to do it if you want to.
