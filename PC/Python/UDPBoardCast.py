import socket 


class UDPBC:
   #port number is 4001 as default
    def __init__(self,m_port=4001):#construct function
        self.port=int(m_port)

    def boardcast(self,m_prot,m_message):
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


    def getIPAddr(self):#get ip addr
        host=socket.gethostname()
        return host

    def getIPSpace(self,hostname):#get ip space
        length=hostname.length
        return ipspace
