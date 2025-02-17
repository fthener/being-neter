import socket
def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return "开放" if result == 0 else "关闭"

ports = [80, 443, 22]
for port in ports:
    print(f"端口 {port} : {check_port(port)}")
