import time
import socket
from concurrent.futures import ThreadPoolExecutor

open_ports = []
def scan(ip, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((ip, port))
            open_ports.append(port)
    except:
        pass
ip = "127.0.0.1"
port_range = "0-100"
threads_count = 50
timeout = 1
start_port, end_port = map(int, port_range.split("-"))
start_time = time.time()
with ThreadPoolExecutor(max_workers=threads_count) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan, ip, port, timeout)
for port in sorted(open_ports):
    print(f"Port {port} is open")
end_time = time.time()
print(f"\nScanned ports in {round(end_time - start_time, 2)} seconds")