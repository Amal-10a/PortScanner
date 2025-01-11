import socket
from datetime import datetime 

target = input("Enter Domain Name OR IP Address :")
ip_address = socket.gethostbyname(target)
print(f"SCANNING {target} ({ip_address})")

start_time = datetime.now()

try:
    for port in range(1, 1025): 
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     socket.setdefaulttimeout(1)
     result = sock.connect_ex((ip_address, port))
     if result == 0:
         print(f"Port {port} Open") 
     sock.close()

except KeyboardInterrupt:
    print("\n The program has been stopped")
    exit()

except socket.gaierror:
    print("\n Error in Domain name")
    exit()

except socket.error:
    print("\n Unable to connect to server")
    exit()

end_time = datetime.now()
print(f"Examination Time :{end_time - start_time}")
