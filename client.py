from uuid import getnode as get_mac
import socket
import threading
import time
from table import *
import datetime
import pickle
import random

class Record():
    def __init__(self, iden, longitude = 27.7, latitude = 27.7,active=False,neighbors= {},lifetime = datetime.datetime.now() ,timestamp = datetime.datetime.now()): 
        self.id = iden
        self.location = (longitude,latitude)
        self.timestamp = timestamp
        self.neighbors = neighbors
        self.lifetime = lifetime
        self.active = active

class Packet():
    def __init__(self, signature, sender, data):
        self.signature = signature
        self.sender = sender
        self.data = data
        
class Device:
    def __init__(self,conf):
        self.DeviceID = 'Drone 1'
        for line in conf:
            
            if line.startswith("active"):
              if(line.split(" ")[-1].strip("\r\n") == "1"):
                  self.active=True
              else:
                  self.active=False
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
           
              
                
        #self.active = False    
        self.battery = 100
        self.next_to_be_replaced = self.DeviceID
        self.replace_lifetime = 0
        self.flag = {}
        self.timout = 10
        self.queue = []
        self.lifetime = 0
        self.longitude = 1234
        self.latitude = 200
        self.neighbors = {}
        self.table = Table({self.DeviceID:Record(self.DeviceID,self.longitude,self.latitude,self.active,self.neighbors,self.lifetime,datetime.datetime.now())})
            
   
    def build_packet(self):
        pack = Packet(self.header, self.DeviceID , self.table)
        data_string = pickle.dumps(pack)
        pack = self.crypto_packet(data_string)
        
        return self.crypto_packet(data_string)

    def parse_packet(self, buff):
        # Returns Packet object
        buff = self.crypto_packet(buff)
        pack = pickle.loads(buff)
        self.neighbors_update(pack.sender)
        
        return pack.data 

    def crypto_packet(self, buf):
        newVal = ''
        for i in xrange(len(buf)):
            newVal += (chr(ord(buf[i]) ^ ord(self.key[i % len(self.key)])))

        return newVal


   
    def update_myself(self):
        while True:
            timestamp = datetime.datetime.now()
            
            self.table.engage(Table({self.DeviceID:Record(self.DeviceID,
                                                          self.longitude,
                                                          self.latitude,
                                                          self.active,
                                                          datetime.datetime.now(),
                                                          self.lifetime)}))            
            time.sleep(5)
            
    def update_table(self, new_table):
        self.table.engage(new_table)
        
    def kill_device():
        pass

    def is_dead():
        pass

    def calculate_remainingTime(self):
        ###### in real-life checks directly with hardware
        import random
        print "calculating time"
        self.battery = self.battery - random.randint(1,3) 
        self.lifetime = self.battery*15/60
        time.sleep(20)

    def sort_queue():
        for dev in table.devices:
            if dev.lifetime < self.replace_lifetime:
                self.next_to_be_replaced = dev.DeviceID
                self.replace_lifetime = dev.lifetime


    def emergency():
        self.lifetime = 1

    def neighbors_update(self, deviceID):
        self.neighbors[deviceID] = datetime.datetime.now()

    # Check if need to delete neighbor who was inactive for 1 min.
        for deviceID in self.neighbors.keys():
            if (datetime.datetime.now() - self.neighbors[deviceID]) > datetime.timedelta(0, 60, 0):
                self.neighbors.pop(deviceID,None)
            
    def actiavte():
        this.active=True
        return

        
    def how_much_alive():
        pass


    def alert_problem():
        pass

   
            

    ### needed to run on its own thread
    def recvmsg(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind(("", int(self.port)))
        while True:
            buff, addr = client.recvfrom(1024)
            buff = self.parse_packet(buff)            
            self.update_table(buff)
            self.table.print_nicely()

##### needs to be on a thread of its own            
    def sendmsg(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        server.settimeout(0.2)
    
        
        
        while True:
            
            message = self.build_packet()
            server.sendto(message, ('<broadcast>', int(self.port)))            
            time.sleep(float(self.timer_to_update))        

        


            
def main():
    conf_file = open("conf.txt",'r').readlines()
   
    device = Device(conf_file)

    
    threading.Thread(target = device.recvmsg,args = ()).start()
    threading.Thread(target = device.sendmsg,args = ()).start()
    threading.Thread(target = device.calculate_remainingTime).start()
    threading.Thread(target = device.update_myself).start()



if __name__=="__main__":
    main()


    
