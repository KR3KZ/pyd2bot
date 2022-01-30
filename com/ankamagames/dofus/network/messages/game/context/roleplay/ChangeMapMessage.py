from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChangeMapMessage(INetworkMessage):
    protocolId = 3431
    mapId:int
    autopilot:bool
    
    
