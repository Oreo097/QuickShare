import socket 


class UDPBC:
   #port number is 4001 as default
    def __init__(self,m_port=4001,):#construct function
        self.port=int(m_port)
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def boardcast(self,m_prot,m_message):#main function of this class
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.sendto(m_message,(self.getIPSpace(self.getIPAddr()),self.port))

    def getIPAddr(self):#get ip addr
        host=socket.gethostname()
        return host

   
    def getIPSpace(self,hostname):#get ip space
        hostname_length=len(hostname)
        hostname[hostname_length-1]='5'#change ip addrress to udp boardcast ip address
        hostname[hostname_length-2]='5'
        hostname[hostname_length-3]='2'
        hostspace=hostname
        print("hostspace:"+hostspace)
        return hostspace
