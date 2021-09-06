# Andrew Johnston's Project 1 

# Setup for repositories
The first step of the project was to make sure that SSH key was tied to github so the website and the server knew it was talking to themselfs. 
The first step was to create a ssh key with the command "ssh-keygen -t ed25519 -C "johnston.124@wright.edu"". After that I moved to copy the key with the command "cat id_25519.pub" and that spitted out the key. After that I just moved to github and pasted it to the ssh keygen tab. After this was done it was a simple command "git clone git@github.com:WSU-kduncan/ceg3120-AndrewJohnston12.git" to clone my repo.

# Users, Folders, Permissions
the user is the one that that access to the server. You can add more users but you have to make sure they have access to the keys so they can log into the server 
permissions of a file can be found by the command "ls -lah" and they break down into user, group, and all users and you can change the permissions of files with commands like "chmod 600 ceg3120-f21.pem"
folders can be broken be down into directory and files like "root" and "boot" are the storage of basic files to run your server 
# SSH key directions
using the "cd .ssh" command you can see all the keys the authorized keys and if you look up the setup for repositories you can see how to set up the ssh for AWS.

# Clone usage & description 
the "clone" command is use for claning a local or remote repository,
cloning a bare repository and other uses. Git Clone is primarily used to point to an existing repo and make a clone of that repo at a new directory.

# init usage & description 
the int command is parent of all linux processes. int stands for initializations. in simple words the roe of init is to create processes from script stored in the file /etc/inttab 

# add usage & description 
the add command is the first stage of the add, commit, push commands and "git add" command takes a modified file in your working directory and places the modified version in a staging area.

# commit usage & description
the commit command is the second stage of the add, commit, push commands and "git commit" takes everything from the staging area and makes a permanent snapshot of the current state of your repositry that is associated with the unique identifier.

# push usage & description 
the push command is the last stage of the add, commit, push commands and "git push" just moves the changes to github 