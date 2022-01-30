from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CurrentMapMessage(INetworkMessage):
    protocolId = 9325
    mapId:int
    mapKey:str
    
    
