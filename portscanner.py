import socket
import argparse
parser = argparse.ArgumentParser( description = "Customized Port Scanner made using Sockets.\n"
"Uses a single address at a time.",
epilog="Made by Priyansh.")

parser.add_argument("-pl", help="Lower limit of port scanning. Can also use this if a single port is to be checked.", type=int)
parser.add_argument("-ph", help="Upper limit of port scanning. Ignore if a single port is to be checked.", type=int)
parser.add_argument("-ip", help="I.P. address array of victim.", required=True, nargs="+")
parser.add_argument("-proto", default="tcp" , help="Protocol of service of the port. Default is tcp.", type=str)
parser.add_argument("-pArr" , help="A random list of ports, separated by spaces.", nargs="+", type=int)

args = parser.parse_args()

host = args.ip
l = args.pl
h = args.ph
protocol = args.proto
portlist = args.pArr

if h == None:
    h = l;

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


def lowhigh(a,b):
    for port in range(a,b +1):
        if scan(host, port):
            print(port, "is open.")
        else:
            print(port, "is closed.")
        service(port, protocol)

def portarray(array):
    for port in array:
        if scan(host, port):
            print(port, "is open.")
        else:
            print(port, "is closed.")
        service(port, protocol)

if l == None:
    print("\n")
    print("Using specified array of ports...")
    portarray(portlist)
    print("\n")
else:
    print("\n")
    print("Using range of ports..")
    lowhigh(l,h)
    print("\n")
