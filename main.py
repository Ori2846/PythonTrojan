import socket
def get_ip():
    global IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
get_ip()

print(IP)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
local_ip = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + local_ip)