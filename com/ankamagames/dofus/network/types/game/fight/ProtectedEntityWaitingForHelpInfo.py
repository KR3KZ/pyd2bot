from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ProtectedEntityWaitingForHelpInfo(INetworkMessage):
    protocolId = 2847
    timeLeftBeforeFight:int
    waitTimeForPlacement:int
    nbPositionForDefensors:int
    
    
