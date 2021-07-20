import socket
import argparse
from colorama import Fore, Back, Style
import time

start = time.time()
print("\n")
print(Fore.CYAN+ Style.BRIGHT +  "Scanning started." + Fore.RESET)

parser = argparse.ArgumentParser( description = "Port Scanner made using sockets, it uses a single IP address at a time.",
epilog="Made by Priyansh.")

parser.add_argument("-ip", help="I.P. address of victim.", required=True)
parser.add_argument("-pA" , help="Intakes a random amount of ports, separated by spaces.", nargs="+", type=int)
parser.add_argument("-pR", help="Intakes two ports separated by spaces which are used as the bounds of scanning. (Both inclusive)", type=int, nargs="+")
parser.add_argument("-proto", default="tcp" , help="Protocol of service of the port. Default is tcp.", type=str)
parser.add_argument("-op" , help="Returns a list of open ports and nothing if no ports are open. Use with either -pA or -pR.", action="store_true")

args = parser.parse_args()

host = args.ip
portsRange = args.pR
protocol = args.proto
portsArray = args.pA
open = args.op

def scan(host, port):
    s = socket.socket()
    s.settimeout(0.13)
    try:
        s.connect((host, port))
        return True
    except:
        return False

def service(port, protocol):

    try:
        serviceName = socket.getservbyport(port, protocol);
        print("Service running at %d : %s"%(port, serviceName));
    except:
        print(Fore.RED + "Protocol not found." + Fore.RESET)

def portRange(array):
    for port in range(array[0],array[1] +1):
        if scan(host, port):
            print(Fore.GREEN + "Port", port, "is open." + Fore.RESET)
        else:
            print("Port",port, "is closed.")
        service(port, protocol)

def openRange(array):
    for port in range(array[0],array[1] +1):
        if scan(host, port):
            print(Fore.GREEN + "Port", port, "is open." + Fore.RESET)
            service(port, protocol)

def portArray(array):
    for port in array:
        if scan(host, port):
            print(Fore.GREEN + "Port", port, "is open." + Fore.RESET)
        else:
            print("Port", port, "is closed.")
        service(port, protocol)

def openArray(array):
    for port in array:
        if scan(host, port):
            print(Fore.GREEN + "Port", port, "is open." + Fore.RESET)
            service(port, protocol)

if portsArray:
    openArray(portsArray) if open else portArray(portsArray)
elif portsRange:
    try:
        openRange(portsRange) if open else portRange(portsRange)
    except:
        print(Fore.RED + "Please provide valid arguments.")
end = time.time()

print(Style.BRIGHT + Fore.CYAN + "Execution completed in", round(end-start , 3), "seconds.")
print("\n")
