*Softwarebot' is the bot I use on my discord server.*

**Versions:**   
the different versions are represented by the folders at the root of the github branch. For example, to get the complete code of version 1.3, you need to 
access the `softwarebot1.3-github` folder. 

**File information:**   
When you access the directory for a release, there are several files. The file with the `.py` extension (in the above example `softwarebot1.3-github.py`) is 
simply the complete Softwarebot code. Please note that if you wish to use it and/or modify the code, you must enter the required information. Still in the 
example of version 1.3, the mention `token_number` as indicated at the top corresponds to the token of your bot discord: this one will thus change each 
time. The other elements to modify are usually indicated from the second or third line of the python file code.     

**The Procfile file** in the directory contains the command to execute according to the hosting service you use: since the launch command of a python file 
is `python3 file.py`, it is this last launch command that we will indicate in our Procfile. If you change the name of your file, you must also change the 
name inside your Procfile.  

**The last file in the directory is `requirements.txt`.**
This one is mainly used to tell your hosting service which python libraries to install. In this case, Softwarebot uses the python library `discord.py`, so 
we write it as shown in the file.       

**So when you install Softwarebot on a hosting service, you MUST send these three files to the service.
If you have any problems, don't hesitate to contact me! :)**
    
*Please note that when you use any of the code here, you must mention the following to me if possible:* 
    
Made by Lushketchup8624 | https://github.com/malwprotector


