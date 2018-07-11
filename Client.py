from uuid import getnode as get_mac
import socket
import threading
import time
from table import *
import datetime

class Record():
   def __init__(self, iden, longitude = 27.7, latitude = 27.7,active=False,neighbors= {},lifetime = datetime.datetime.now() ,timestamp = datetime.datetime.now()): 
        self.id = iden
        self.location = (longitude,latitude)
        self.timestamp = timestamp
        self.neighbors = neighbors
        self.lifetime = lifetime
        self.active = active
        
class Device:
    def __init__(self,conf):
        self.DeviceID = get_mac()

        for line in conf:
            if line.startswith("encryption_key"):
                self.key=line.split(" ")[-1].strip("\r\n")
            if line.startswith("packet_secret_header"):
                self.header=line.split(" ")[-1].strip("\r\n")
            if line.startswith("Minimun_number_of_devices"):
                self.min_num_of_devices=line.split(" ")[-1].strip("\r\n")
            if line.startswith("port_to_communicate"):
                self.port=line.split(" ")[-1].strip("\r\n")
            if line.startswith("update_time"):
                self.timer_to_update=line.split(" ")[-1].strip("\r\n")
            
        self.flag = {}
        self.active = False
        self.timout = 10
        self.queue = []
        self.lifetime = 0
        self.longitude = 222
        self.latitude = 200
        self.neighbors = []
        self.table = Table({self.DeviceID:Record(self.DeviceID,self.longitude,self.latitude,self.active,self.neigbors,self.lifetime,datetime.datetime.now())})
        

     def recvmsg():
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind(("", self.port))
        while True:
            buff, addr = client.recvfrom(1024)
            buff= crypto_packet(buff)
            if verify_key(buff)
                buff= parse_packet(buff)
            else
                continue
            
    def sendmsg():
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        server.settimeout(0.2)
    
        message = build_packet(self.table)
        
        while True:
            server.sendto(message, ('<broadcast>', self.port))
            
            time.sleep(self.timer_to_update)
            
    def build_packet():
        pass
    def parse_packet():
        pass
    
    def crypto_packet(buff):
        pass
    
    def calculate_Timestamp(table):
        pass

    def update_myself(self):
        timestamp = datetime.datetime.now()
        self.table.engage({self.DeviceID:Record(self.DeviceID,self.longitude,self.latitude,self.active,datetime.datetime.now(),self.lifetime)})

    def update_table(self, new_table):
        
        buff = decrypt_packet(buff)
        self.table.engage(new_table) 
        pass

    def kill_device():
        pass

    def is_dead():
        pass

    def calculate_remainingTime():
        pass

    def sort_queue():
        pass


    def raise_swapInterupt(DeviceId):
        pass

    def actiavte():
        this.active=True

        return

    def how_much_alive():
        pass

    def verify_key(buff):
        if(buff[:len(self.header)] == self.header):
            return True
        else:
            return False
    

    def alert problem():
        pass

   
            
        

        


            
def main:
    conf_file = open("C:\\conf.txt",'r').readlines()
   
    device = Device(conf_file)

    
    threading.Thread(target = recvmsg,args = ()).start()
    threading.Thread(target = sendmsg,args = ()).start()
     


if __name__=="__main__":
    main()
