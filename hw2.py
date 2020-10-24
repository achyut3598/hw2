import socket
import sys
import os

#get current path
path = os.getcwd()
rel = "/home/data/"
out = "/home/output/"
new_path = path + out
path = path + rel
grand_total = 0
length = []
pos = 0
files = []

for f in os.listdir(path):
    if f.endswith(".txt"):
        files.append(f)
        newf = path + f
        file = open (newf,"r")
        data = file.read()
        words = data.split()
        length.append(len(words))
        strlen = len(words)
        with open(new_path+'result.txt','a') as file:
            file.write("%s %s \n" % (f, strlen))
            file.close()
        grand_total = grand_total + len(words)
pos = length.index(max(length))
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
with open(new_path+'result.txt','a') as file:
            file.write("Total number of words %s \n" % grand_total) 
            file.write("The biggest file is %s with %s words \n" % (files[pos], length[pos]))
            file.write("The ip address is %s \n" % ip)
            file.close()

read_file = open (new_path+'result.txt',"r")
strings = read_file.read()
print (strings)

    
    
"""with open(new_path+'\\ciphertext.txt','w') as file:
            file.write(cipher)
            file.close()"""
