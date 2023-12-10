import socket
import sys


def GET(host, port, user):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((host, port))
            print(f"Host {host} is online.")

            request = f"GET {user} HTTP/1.1\r\nHOST: {host}\r\n\r\n"
            sock.sendall(request.encode())

            response = sock.recv(4096)
            
        return response.decode()

    except ConnectionRefusedError:
        print(f"Host {host} is offline.")
    except Exception as e:
        print(f"Error checking host {host}: {e}")


def POST(host, port, user_name, user_age):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((host, port))
            print(f"Host {host} is online.")
            data = user_name + " " + user_age
            request = f"POST {data} HTTP/1.1\r\nHOST: {host}\r\n\r\n"
            sock.sendall(request.encode())

            response = sock.recv(4096)
            
        return response.decode()

    except ConnectionRefusedError:
        print(f"Host {host} is offline.")
    except Exception as e:
        print(f"Error checking host {host}: {e}")
    

if __name__ == "__main__":
    host = "localhost"
    port = 8080
    method = sys.argv[1]
    
    if method == "HELP":
        print("Enter 'GET user_id' or 'POST user_name user_age' to simulate a request.")

    elif method == "GET":
        user = sys.argv[2]
        decoded_response = GET(host, port, user)

    elif method == "POST":
        user_name = sys.argv[2]
        user_age = sys.argv[3]
        decoded_response = POST(host, port, user_name, user_age)

    print(decoded_response)
