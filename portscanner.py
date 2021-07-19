import socket
import argparse
from colorama import Fore, Back, Style
import time

start = time.time()
print("\n")
print(Fore.CYAN+ Style.BRIGHT +  "PortScanner started." + Fore.RESET)

parser = argparse.ArgumentParser( description = "Customized Port Scanner made using Sockets. Uses a single address at a time.",
epilog="Made by Priyansh.")

parser.add_argument("-ip", help="I.P. address of victim.")
parser.add_argument("-pA" , help="Inakes a random amount of ports, separated by spaces.", nargs="+", type=int)
parser.add_argument("-pR", help="Intakes two ports separated by spaces which are used as the bounds of scanning. (Both inclusive)", type=int, nargs="+")
parser.add_argument("-proto", default="tcp" , help="Protocol of service of the port. Default is tcp.", type=str)
parser.add_argument("-op" , help="Returns a list of open ports and nothing if no ports are open. Use with either -pA or -pR.", action="store_true")

args = parser.parse_args()

host = args.ip
portsRange = args.pR
protocol = args.proto
portsArray = args.pA
open = args.op

if host:
    def scan(host, port):
        s = socket.socket()
        try:
            s.connect((host, port))
        except:
            return False
        else:
            return True

    def service(port, protocol):

        try:
            serviceName = socket.getservbyport(port, protocol);
            print("Service at %d : %s"%(port, serviceName));
        except:
            print(Fore.RED + "Protocol not found.")

    def portRange(array):
        for port in range(array[0],array[1] +1):
            if scan(host, port):
                print("Port", port, "is open.")
            else:
                print("Port",port, "is closed.")
            service(port, protocol)

    def openRange(array):
        for port in range(array[0],array[1] +1):
            if scan(host, port):
                print("Port", port, "is open.")
                service(port, protocol)

    def portArray(array):
        for port in array:
            if scan(host, port):
                print("Port", port, "is open.")
            else:
                print("Port", port, "is closed.")
            service(port, protocol)

    def openArray(array):
        for port in array:
            if scan(host, port):
                print("Port" , port, "is open.")
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
