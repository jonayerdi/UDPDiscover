from socket import *

ss = socket(AF_INET, SOCK_DGRAM) 
ss.bind(('0.0.0.0', 45454))

cs = socket(AF_INET, SOCK_DGRAM)  
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) 
cs.sendto(b'DISCOVER', ('255.255.255.255', 54545))
cs.close()

while True:
    (bytes, address) = ss.recvfrom(1024)
    print(f'{address[0]}: {bytes}')
