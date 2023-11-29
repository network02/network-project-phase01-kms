
import socket
import sys


def check_host_online(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((host, port))
            print(f"Host {host} is online.")
    except ConnectionRefusedError:
        print(f"Host {host} is offline.")
    except Exception as e:
        print(f"Error checking host {host}: {e}")


if __name__ == "__main__":
    host = sys.argv[1]
    for i in range(2, len(sys.argv)):
        port = int(sys.argv[i])
        check_host_online(host, port)
