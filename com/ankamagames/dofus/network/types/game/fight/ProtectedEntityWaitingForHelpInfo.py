from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ProtectedEntityWaitingForHelpInfo(INetworkMessage):
    protocolId = 2847
    timeLeftBeforeFight:int
    waitTimeForPlacement:int
    nbPositionForDefensors:int
    
    
