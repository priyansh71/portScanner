import socket
import argparse
parser = argparse.ArgumentParser( description = "Customized Port Scanner made using Sockets. Uses a single address at a time.",
epilog="Made by Priyansh.")

parser.add_argument("-pR", help="Takes two integers separated by spaces which are used as the bounds of port scanning. (Both inclusive)", type=int, nargs="+")
parser.add_argument("-ip", help="I.P. address array of victim.", required=True)
parser.add_argument("-proto", default="tcp" , help="Protocol of service of the port. Default is tcp.", type=str)
parser.add_argument("-pA" , help="Takes a random list of ports, separated by spaces.", nargs="+", type=int)
parser.add_argument("-op" , help="Returns the open ports. Use with either -pA or -pR", action="store_true")

args = parser.parse_args()

host = args.ip
portsRange = args.pR
protocol = args.proto
portsArray = args.pA
open = args.op

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
        print("Service at :%d => %s"%(port, serviceName));
    except:
        print("Protocol not found.")


def portRange(array):
    for port in range(array[0],array[1] +1):
        if scan(host, port):
            print(port, "is open.")
        else:
            print(port, "is closed.")
        service(port, protocol)

def openRange(array):
    for port in range(array[0],array[1] +1):
        if scan(host, port):
            print(port, "is open.")
            service(port, protocol)


def portArray(array):
    for port in array:
        if scan(host, port):
            print(port, "is open.")
        else:
            print(port, "is closed.")
        service(port, protocol)

def openArray(array):
    for port in array:
        if scan(host, port):
            print(port, "is open.")
            service(port, protocol)


if portsArray:
    print("\n")
    print("Using specified array of ports...")
    openArray(portsArray) if open else portArray(portsArray)
elif portsRange:
    print("\n")
    print("Using limiting range of ports..")
    openRange(portsRange) if open else portRange(portsRange)
