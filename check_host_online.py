import socket
import sys


def check_host_online(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((host, port))
            print(f"Host {host}:{port} is online.")
            service_name = socket.getservbyport(port)
            print(f"Service name running on this port: {service_name}")
    except ConnectionRefusedError:
        print(f"Host {host}:{port} is offline.")
    except Exception as e:
        print(f"Error checking host {host}:{port}: {e}")


if __name__ == "__main__":
    USEFUL_PORTS = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 119, 123, 143, 161, 194, 443, 546, 547]
    host = sys.argv[1]

    if sys.argv[1] == "HELP":
        print("Enter 'www.example.com all' or 'www,example.com port_numbers' to simulate a request.")
    elif sys.argv[2] == "all":
        for port in USEFUL_PORTS:
            check_host_online(host, port)
    else:
        for port in sys.argv[2:]:
            check_host_online(host, int(port))
