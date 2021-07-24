import socket
import argparse
import time

start = time.time()

parser = argparse.ArgumentParser()

parser.add_argument("-ip", required=True)
parser.add_argument("-pR", type=int, nargs="+")
parser.add_argument("-op" , action="store_true")

args = parser.parse_args()

host = args.ip
portsRange = args.pR
open = args.op

def scan(host, port):
    s = socket.socket()
    s.settimeout(0.049)
    try:
        s.connect((host, port))
        return True
    except:
        return False

def openRange(array):
    for port in range(array[0],array[1] +1):
        if scan(host, port):
            print(port, ": open.")

if open:
    openRange(portsRange)

end = time.time()

print(round(end-start , 3), "seconds.")
