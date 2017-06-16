#!env/bin/python
import socket
import fcntl
import struct
from matterhook import Webhook

interface = "wlan0"
mwh = Webhook('https://mattermost_server', 'in_hook')
mwh.username = 'Raspberry PI'
channel = 'admins'


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
                            s.fileno(),
                            0x8915,
                            struct.pack('256s', ifname[:15])
                            )[20:24])

if __name__ == "__main__":
    ip = get_ip_address(interface)
    msg = "Server successfully loaded, wlan0 interface ip: "
    mwh.send(msg + ip, channel=channel)
