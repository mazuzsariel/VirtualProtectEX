import datetime

class Device():
    def __init__(self, iden, longitude = 27.7, latitude = 27.7,timestamp = datetime.datetime.now()): 
        self.id = iden
        self.location = (longitude,latitude)
        self.timestamp = timestamp
        self.neighbors = neighbors
        self.lifetime = lifetime
        
class Table():
    def __init__(self,devices):
        self.devices = devices
        
    def update_(self,i):
        """update table data of device id"""
        pass
    
    def engage(self,new_table):
        """get new table, compare and update table data"""
        # Run Over new table
        for key in new_table.devices.keys():
            # Check if Device is not in the table
            if key not in self.devices:
                self.new_record(key,new_table.devices[key])
            else:
                d = compare_devices(self.devices[key],new_table.devices[key])
                self.devices[key] = d
                
    def new_record(self,key,data):
        self.devices[key] = data
        
    def send_broadcast(self):
        """broadcast table"""
        pass
    
    def print_nicely(self):
        for i in self.devices:
            print "\nid:  {}\nlocation:  ({},{})\ntime: {}".format(self.devices[i].id,self.devices[i].latitude,self.devices[i].longtiude,self.devices[i].time)
            
def compare_devices(d1,d2):
    if d1.time > d2.time:
        return d1
    else:
        return d2
    
def main():
    time_now = datetime.datetime.now()
    d1 = Device("111", 36.38, 45.89,time_now-datetime.timedelta(seconds=100))
    d2 = Device("222", 38.13, 44.25,time_now-datetime.timedelta(seconds=50))
    d3 = Device("333", 33.54, 24.83,time_now-datetime.timedelta(seconds=40))
    d4 = Device("444", 34.17, 54.89,time_now-datetime.timedelta(seconds=30))

    t1 = Table({"111":d1,"222":d2,"333":d3,"444":d4})

    d1 = Device("111", 10, 10,time_now-datetime.timedelta(seconds=0))
    d2 = Device("222", 20, 20,time_now-datetime.timedelta(seconds=0))
    d3 = Device("333", 33.54, 24.83,time_now-datetime.timedelta(seconds=100))
    d4 = Device("444", 34.17, 54.89,time_now-datetime.timedelta(seconds=100))

    t2 = Table({"111":d1,"222":d2,"333":d3,"444":d4})

    d1 = Device("555", 40, 40,time_now-datetime.timedelta(seconds=0))

    t3 = Table({"555":d1,"222":d2,"333":d3,"444":d4})
    
    t1.engage(t2)
    t1.engage(t3)
    print t1.print_nicely()

if __name__ == '__main__':
    main()
