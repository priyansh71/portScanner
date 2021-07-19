import socket
import argparse
import time

start = time.time()

parser = argparse.ArgumentParser()

parser.add_argument("-ip", help="I.P. address of victim.", required=True)
parser.add_argument("-pR", help="Intakes two ports separated by spaces which are used as the bounds of scanning. (Both inclusive)", type=int, nargs="+")
parser.add_argument("-op" , help="Returns a list of open ports and nothing if no ports are open. Use with either -pA or -pR.", action="store_true")

args = parser.parse_args()

host = args.ip
portsRange = args.pR
open = args.op

def scan(host, port):
    s = socket.socket()
    s.settimeout(0.07)
    try:
        s.connect((host, port))
        return True
    except:
        return False

def openRange(array):
    for port in range(array[0],array[1] +1):
        if scan(host, port):
            print("Port", port, "is open.")

if open:
    # try:
        openRange(portsRange)
    # except:
    #     print("Please provide valid arguments.")
end = time.time()

print("Execution completed in", round(end-start , 3), "seconds.")
print("\n")
