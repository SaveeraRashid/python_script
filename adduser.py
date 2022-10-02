#!/usr/bin/env python3

from shutil import chown
import distro
import pwd
import os
import subprocess
import sys


release=distro.id()
print(release)

users=[]
paths=[]
n=int(input("Enter the number of users you want to add: "))

print("Enter\n 1: Add user \n 2: Delete User")
opt=input()

for i in range(1,n+1):
        print("Enter User",i)
        u=input()
        users.append(u)
        if u=="":
                print("Username is empty")
                exit()
        print("Enter Public key file paths for user", i)
        p=input()
        paths.append(p)
        if p=="":
                print("Public Key File name is empty")
                exit()
        print("User",u)
        print("Path",p)

        if release=='ubuntu':
                if opt=="1":
                        try:
                                pwd.getpwnam(u)
                        except KeyError:
                                print("User does not exist")
                        else:
                                print("User Exists")
                                exit()
os.system("sudo" + " "+ " adduser"+" "+u)
                        os.system('echo "%s  ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers' %(u))
                        parent_dir="/home/"+u+"/.ssh"
                        os.system( "sudo mkdir " + parent_dir )
                        os.system("sudo chmod 777 "+ parent_dir)
                        os.system("sudo chown " + u + " " + parent_dir)
                        file=parent_dir +"/authorized_keys"
                        os.system("sudo touch " + file)
                        os.system("sudo chmod 666 " + file)
                        os.system("sudo chown "+u+" "+file)
                        os.system(' sudo cat %s >> %s' %(p,file))
                if opt=="2":
                        try:
                                pwd.getpwnam(u)
                        except KeyError:
                                print("User Doesnot Exists")
                                exit()
                        else:
                                print("User Exists")
                                os.system("sudo deluser --remove-home "+u)
        if release=='centos':
                if opt=="1":
                        try:
				pwd.getpwnam(u)
                        except:
                                print("User Doesnot Exist")
                        else:
                                print("User Exists")
                                exit()
                        os.system("sudo adduser "+u)
                        os.system("sudo passwd "+u)
                        os.system('echo "%s  ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers' %(u))
                        parent_dir="/home/"+u+"/.ssh"
                        os.system("sudo mkdir "+parent_dir)
                        os.system("sudo chmod 777 "+parent_dir)
                        os.system("sudo chown %s : %s  %s" %(u,u,parent_dir))
                        file=parent_dir+"/authorized_keys"
                        os.system("sudo touch "+file)
                        os.system("sudo chmod 666 "+file)
                        os.system("sudo chown  %s : %s %s" %(u,u,file))
                        os.system("sudo cat %s >> %s" %(p,file))
                if opt=="2":
                        try:
                                pwd.getpwnam(u)
                        except KeyError:
                                print("User Does not exists")
				exit()
                        else:
                                print("User Exists")
                                os.system("sudo userdel -r "+u)
