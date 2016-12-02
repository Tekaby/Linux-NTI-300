#!/bin/python
import os

def install_apache():
    print("installing apache server")
    os.system('sudo yum -y install httpd')


    print("enabling apache server")
    os.system('sudo systemctl enable httpd.service')

    print("starting apache server")
    os.system('sudo systemctl start httpd.service')


    print("If you open the security settings for port 80 on your server, you should see the apache start page")
install_apache()

def install_dirty_cow():
    os.system('sudo yum clean all')
    os.system('sudo yum update kernel') 
    os.system('sudo reboot')

def verify_dirty_cow():
    os.system('sudo rpm -q --changelog kernel | grep CVE-2016-5195')
verify_dirty_cow()

def install(package):
    os.system('sudo yum -y install ' + package)

def install_git():
    os.system('sudo yum -y install git; git clone https://github.com/nic-instruction/NTI-300/')
    print("a clone of the NTI-300 reposatory is now sitting in this dir, along with a copy of this script \n")
    print("For a git command line cheet sheet check out https://services.github.com/kit/downloads/github-git-cheat-sheet.pdf \n")
    print("Basic commands:
      git pull            # will get you repo updates
      git add .           # will add files in your dir
      git add [dirname]/* # will add files under a new dir
      git commit -m "your comment" # will commit your code to your changes
      git push            # will push your code to a reposatory
      git pull            # will pull down new reposatory updates")

