import datetime
import time
import copy

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
        
    def toJSON(self):
        d =  copy.deepcopy(self.__dict__)
        d["modifed"] = time.mktime(d["modifed"].timetuple())
        for i in d["devices"]:
            d["devices"][i] = d["devices"][i].toJSON()
        print d
        return d
    
    def print_nicely(self):
        print '#########################TABLE#########################'
        try:
            for i in self.devices:
                print "\nid:  {}\ocation:  {}\ntime: {}\active {}".format(self.devices[i].id,self.devices[i].location,self.devices[i].timestamp,self.devices[i].active)
        except Exception as e:
            print e

     
def compare_devices(d1,d2):
    print d1
    if d1.timestamp > d2.timestamp:
        return d1
    else:
        return d2
