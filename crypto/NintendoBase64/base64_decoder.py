
from base64 import b64decode

flag = open('output.txt').read().replace(' ','').encode()

while flag[:5] != b'CHTB{':
	flag = b64decode(flag)
	
print(flag)


