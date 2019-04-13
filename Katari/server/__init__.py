import socket
from Katari.sip import SipMessage

class SipServer:


    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.application = None
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host,self.port))


    def start(self):
        self.listener()


    def listener(self):
        while True:
            data = self.socket.recvfrom(1024)
            message = SipMessage(data[0])
            if message.sip_type != None:
                response = self.application._server_run(message)
                self.socket.sendto(response.export().encode(),data[1])


    def register_app(self,app):
        self.application = app

    def parse_sip(self,message):
       return SipParser(message)


















