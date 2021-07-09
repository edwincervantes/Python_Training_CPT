'''
Author: EJ Cervantes
'''

import sys
import os
import argparse
import traceback
from socket import *

def establishConnection(host, port_start, port_end):
    for port in range(port_start, port_end):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        result = clientSocket.connect_ex((host, port))
        if result == 0:
            print("Port {}:      Open".format(port))
        clientSocket.close()
    
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", help="The host of the Target IP")
        parser.add_argument("--port_start", help="The ports you would like to start at", type=int)
        parser.add_argument("--port_end", help="The port you would like to end at", type=int)
        args = parser.parse_args()

        establishConnection(args.host, args.port_start, args.port_end)

    except:
        print(traceback.format_exc())
        sys.stdout.flush()
        sys.exit(1)
