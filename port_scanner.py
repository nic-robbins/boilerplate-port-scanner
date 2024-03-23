import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose: bool):
		open_ports = []
		host = socket.gethostbyname(target)

		for port in range(port_range[0], port_range[1]):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(5)
				result = s.connect_ex((host, port))

				if result == 0:
						open_ports.append(port)
						if verbose:
								service = ports_and_services.get(port, "Unknown")
								print(f"Open ports for {target}: ")
								print(f"Port: {port} Service: {service}")
						s.close()
						if not verbose:
							print(f"Open ports: {port}")
						else:
							print("No open ports found.")
	
		return open_ports

open_ports = get_open_ports("hackthissite.org", [440, 445], True)

