import socket
from common_ports import ports_and_services


def get_open_ports(target, port_range, verbose = True):
    open_ports = []
    ip = socket.get
    port = range(port_range[0], port_range[1])
    if port in ports_and_services:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(5)
        result = s.connect_ex((ip, port))
            open_ports.append(port)
        def port_scanner(port):
            if s.connect_ex((ip, port)):
                print("The port is closed")
            else:
                print("The ports for", ip, "are", open_ports)
    return(open_ports)

port_scanner(get_open_ports("209.216.230.240", [440, 445]))