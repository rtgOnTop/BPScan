#UltImateHackingTOol
from colorama import Back
import socket
import argparse

print("""
██████╗ ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██████╔╝███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║     ███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝       
  01101101 01100001 01100100 01100101  01100010 01111001        
01110010 01110100 01100111 00111000 00110011 00111000 00110111                                                                         
       \n""") 



def scan_specific_port(host=None, port=None):

  try:
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((host, port))
      s.sendall()
      data = s.recv(1024)
      print(Back.GREEN + f"[+] Port is open at {port}")
  except (ConnectionError):
     print(Back.RED + f"[!] Connection likely refused by firewall or port is not open [{port}]")
  input(Back.RESET + "Exit by clicking enter")
      



def scan_ports_range(host, port, r1, r2): #the parameters are not post to be set, only input sets it


   for i in range(r1, r2): 
      port = i
      try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall() # future malicious payload?
            data = s.recv(1024)

            print(Back.GREEN + f"[+] Port is open at [{port}]")
      except (ConnectionRefusedError):
          print(Back.RED + f"[!] Connection likely refused by firewall or port is not open [{port}]\n")
   input(Back.RESET + "Exit by clicking enter")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Create the parser for the "scanP" command
scan_port = subparsers.add_parser("scanP", help="This is used to signify what function you'll be using")
scan_port.add_argument("--host", type=str, help="The host needed for a port scan")
scan_port.add_argument("--port", type=int, help="The port needed for a port scan")

# Create the parser for the "scanrangeP" command
scan_ports = subparsers.add_parser("scanrangeP", help="Scan a range of ports")
scan_ports.add_argument("--host", type=str, help="The host needed for a port scan")
scan_ports.add_argument("--port", type=int, help="The port needed for a port scan")
scan_ports.add_argument("--range1", type=int, help="The first parameter for the range of ports to be used")
scan_ports.add_argument("--range2", type=int, help="The second parameter for the range of ports to be used")

# Parse the arguments
args = parser.parse_args()

# Execute the appropriate function based on the command
if args.command == "scanP" and __name__ == "__main__":
    scan_specific_port(args.host, args.port)
elif args.command == "scanrangeP" and __name__ == "__main__":
    scan_ports_range(args.host, args.port, args.range1, args.range2)