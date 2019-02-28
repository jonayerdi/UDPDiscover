import socket

REPLY_PORT = 45454
MULTICAST_GROUP = '224.0.21.132'
MULTICAST_PORT = 54545
MULTICAST_TTL = 32

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ss.bind(('', REPLY_PORT))

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 
try:
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except AttributeError:
    pass
try:
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
except AttributeError:
    pass
cs.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
cs.sendto(socket.gethostname().encode('UTF-8'), (MULTICAST_GROUP, MULTICAST_PORT))
cs.close()

while True:
    (bytes, address) = ss.recvfrom(1024)
    print(f'{address[0]}: {bytes}')
