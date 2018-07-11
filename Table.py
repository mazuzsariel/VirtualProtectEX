import datetime

class Device():
    def __init__(self, iden, longitude = 27.7, latitude = 27.7,active=False,neighbors= [],lifetime = datetime.datetime.now() ,timestamp = datetime.datetime.now()): 
        self.id = iden
        self.location = (longitude,latitude)
        self.timestamp = timestamp
        self.neighbors = neighbors
        self.lifetime = lifetime
        self.active = active
        
class Table():
    def __init__(self,devices):
        self.modifed = datetime.datetime.now()
        self.devices = devices
    
    def engage(self,new_table):
        """get new table, compare and update table data"""
        # Run Over new table
        for key in new_table.devices.keys():
            # Check if Device is not in the table
            if key not in self.devices:
                self.new_record(key,new_table.devices[key])
            else:
                self.update_record(key,new_table.devices[key])
    def update_record(self,key,d):
        d = compare_devices(self.devices[key],d)
        self.devices[key] = d
        self.modifed = datetime.datetime.now()
        
    def new_record(self,key,data):
        self.devices[key] = data
        self.modifed = datetime.datetime.now()
    
    def print_nicely(self):
        for i in self.devices:
            print "\nid:  {}\nlocation:  {}\ntime: {}".format(self.devices[i].id,self.devices[i].location,self.devices[i].timestamp)
            
def compare_devices(d1,d2):
    if d1.timestamp > d2.timestamp:
        return d1
    else:
        return d2
    
def main():
    time_now = datetime.datetime.now()
    d1 = Device("111", 36.38, 45.89,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=100))
    d2 = Device("222", 38.13, 44.25,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=50))
    d3 = Device("333", 33.54, 24.83,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=40))
    d4 = Device("444", 34.17, 54.89,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=30))

    t1 = Table({"111":d1,"222":d2,"333":d3,"444":d4})

    d1 = Device("111", 10, 10,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=0))
    d2 = Device("222", 20, 20,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=0))
    d3 = Device("333", 33.54, 24.83,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=100))
    d4 = Device("444", 34.17, 54.89,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=100))

    t2 = Table({"111":d1,"222":d2,"333":d3,"444":d4})

    d1 = Device("555", 40, 40,True,time_now+datetime.timedelta(seconds=10000),time_now-datetime.timedelta(seconds=0))

    t3 = Table({"555":d1,"222":d2,"333":d3,"444":d4})
    
    t1.engage(t2)
    t1.engage(t3)
    print t1.print_nicely()

if __name__ == '__main__':
    main()
