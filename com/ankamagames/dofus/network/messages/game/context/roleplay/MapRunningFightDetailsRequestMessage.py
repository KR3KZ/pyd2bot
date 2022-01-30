from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MapRunningFightDetailsRequestMessage(NetworkMessage):
    protocolId = 8028
    fightId:int
    
    
