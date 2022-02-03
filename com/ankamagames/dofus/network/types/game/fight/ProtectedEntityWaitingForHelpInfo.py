from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ProtectedEntityWaitingForHelpInfo(NetworkMessage):
    timeLeftBeforeFight:int
    waitTimeForPlacement:int
    nbPositionForDefensors:int
    

    def init(self, timeLeftBeforeFight:int, waitTimeForPlacement:int, nbPositionForDefensors:int):
        self.timeLeftBeforeFight = timeLeftBeforeFight
        self.waitTimeForPlacement = waitTimeForPlacement
        self.nbPositionForDefensors = nbPositionForDefensors
        
        super().__init__()
    
    