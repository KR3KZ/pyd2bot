from time import sleep
import socket

from network.message.msg import Msg

#socket_family − This is either AF_UNIX or AF_INET, as explained earlier.

# socket_type − This is either SOCK_STREAM or SOCK_DGRAM.

sock = socket.socket()
auth_host = "54.76.16.121"
# host = "172.65.194.249"
port = 5555
sock.connect((auth_host, port))

sleep(10)

# def sendToserver(msg: Msg):
#     msg.count = counter + 1
#     data = msg.bytes()
#     sock.sendall(data)

# msg = Msg.from_json(
# {'__type__': 'BasicPingMessage', 'quiet': True}
# )
# counter += 1
# sendToserver(msg)
# sleep(5)
