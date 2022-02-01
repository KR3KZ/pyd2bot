from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ProtectedEntityWaitingForHelpInfo(NetworkMessage):
    timeLeftBeforeFight:int
    waitTimeForPlacement:int
    nbPositionForDefensors:int
    
    
