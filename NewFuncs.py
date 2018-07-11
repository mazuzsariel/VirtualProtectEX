def lifetime_sim(self.battary):
    lifetime = self.battary - (random.randint(1,10) / 100.0)
    return lifetime

def neighbor_update(deviceID):
    neighbors[deviceID] = datetime.datetime.now()

    # Check if need to delete neighbor who was inactive for 1 min.
    for deviceID in neighbors.keys():
        if (datetime.datetime.now() - neighbors[deviceID]) > datetime.timedelta(0, 60, 0):
            neighbors.pop(deviceID,None)
