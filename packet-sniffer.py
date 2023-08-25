#Socket module is basically a library in Python which connects 2 nodes a listener and a receiver. 
import socket

'''Here we are loading all the raw packets data from the socket communication module and assigning it to 's'. 
   AF stands for Address Family and here we are using AF_INET which is for IPV4. We can use AF_INET6 for IPv6 packets.
   SOCK_RAW means the raw socket of TCP and IPPROTO_TCP indicates that TCP protocol is being used.
   recv method is used to receive all the data from the socket.Here 65565 is the maximium buffer size it can handle.
'''

s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
  print(s.recvfrom(65565))
