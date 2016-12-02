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

