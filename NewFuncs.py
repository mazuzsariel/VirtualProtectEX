def emergency():
    """
    In case of emergancy. Kick me to the 1st of the queue
    """
    self.lifetime = 1

def neighbor_update(deviceID):
    neighbors[deviceID] = datetime.datetime.now()

    # Check if need to delete neighbor who was inactive for 1 min.
    for deviceID in neighbors.keys():
        if (datetime.datetime.now() - neighbors[deviceID]) > datetime.timedelta(0, 60, 0):
            neighbors.pop(deviceID,None)
