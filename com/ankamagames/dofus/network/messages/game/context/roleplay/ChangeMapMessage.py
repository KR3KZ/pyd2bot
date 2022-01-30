from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChangeMapMessage(NetworkMessage):
    protocolId = 3431
    mapId:int
    autopilot:bool
    
