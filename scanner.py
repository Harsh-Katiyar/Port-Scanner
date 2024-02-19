import argparse
import socket 
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue


init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

N_THREADS = 400

q=Queue()
l=Lock()

host=input(f"Host{RESET}:")
for i in range(1,100):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print(f"{GREEN}[+]{RESET} Connected to {host}:{port}")
    except:
        print(f"{RED}[-]{RESET} Could not connect to {host}:{port}")
    else:
        print(f"{GREEN}[+]{RESET} Connected to {host}:{port}")
        s.close()
        
        
        
        
        
        
        
        
# def Open(host, port):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         s.connect((host, port))
#     except:
#         print(f"{RED}[-]{RESET} Could not connect to {host}:{port}")
#     else:
#         print(f"{GREEN}[+]{RESET} Connected to {host}:{port}")
#         s.close()

# if __name__ == "__main__":
#     host = input(f"{GRAY}Host{RESET}: ")
#     port = int(input(f"{GRAY}Port{RESET}: "))
#     Open(host, port)