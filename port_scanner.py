import socket

def get_open_ports(target, port_range, verbose = True):
    open_ports = []
    host = socket.gethostbyname(target)
    port = range(port_range[0], port_range[1]+1)
    for port in port:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(5)
        result = s.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
    return(open_ports)

get_open_ports("209.216.230.240", [440, 445])