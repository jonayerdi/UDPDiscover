import socket
import struct

REPLY_PORT = 45454
MULTICAST_GROUP = '224.0.21.132'
MULTICAST_PORT = 54545
MULTICAST_TTL = 2

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
try:
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except AttributeError:
    pass
ss.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL) 
ss.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
ss.bind(('', MULTICAST_PORT))
MEMBERSHIP = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
ss.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, MEMBERSHIP)

while True:
    (bytes, address) = ss.recvfrom(1024)
    print(f'{address[0]}: {bytes}')
    ss.sendto(socket.gethostname().encode('UTF-8'), (address[0], REPLY_PORT))
