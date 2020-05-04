import socket
import hashlib
import os
import time
import json

class FTPT:
    
    #mulit-Thread socket transmission class

    def __init__(self,m_file_addr,m_port=4002):
        self.port=m_port
        self.file_addr=m_file_addr


    def setupScoket(self,port):
        #set up socket
        self.socket=socket.socket()
        self.scoket.bind(('localhost',port))
        self.listen()
        print("start,listening")

        #waiting for client connection
        connection=self.socket.accept()
        print("connected")

        #start hand shake
        

