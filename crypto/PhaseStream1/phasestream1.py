#!/usr/bin/python3
import os
#flag = open('flag.txt', 'r').read().strip().encode()

class XOR:
    def __init__(self):
        self.key = os.urandom(4)
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    crypto = XOR()
    print ('Flag:', crypto.encrypt(flag).hex())

if __name__ == '__main__':
    enc_flag = '2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904'
    enc_flag = bytes.fromhex(enc_flag)

    key = b''
    msg_header = b'CHTB{'
    for i in range(len(msg_header)):
        key += bytes([msg_header[i] ^ enc_flag[i]])

    crypto = XOR()
    crypto.key = key
    flag = crypto.decrypt(enc_flag)
    print(flag)
        
