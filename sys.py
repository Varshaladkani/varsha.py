import json
import socket
import getpass
import socket

# created a json file


dict1 = {"hostname": socket.gethostname(),
         "username": getpass.getuser(),
         "ip": socket.gethostbyname(socket.gethostname())
         }
print(dict1)
path = r'/home/varsha/Documents/sys_info.json'

with open("sys_info.json", 'w')as json_file:
    json.dump(dict1,json_file)
