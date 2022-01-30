from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ProtectedEntityWaitingForHelpInfo(NetworkMessage):
    protocolId = 2847
    timeLeftBeforeFight:int
    waitTimeForPlacement:int
    nbPositionForDefensors:int
    
