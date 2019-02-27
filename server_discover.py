from socket import *

ss = socket(AF_INET, SOCK_DGRAM) 
ss.bind(('0.0.0.0', 54545))

while True:
    (bytes, address) = ss.recvfrom(1024)
    print(f'{address[0]}: {bytes}')
    ss.sendto(b'DISCOVER', (address[0], 45454))
