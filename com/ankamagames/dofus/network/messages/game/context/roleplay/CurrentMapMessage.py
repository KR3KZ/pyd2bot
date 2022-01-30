from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CurrentMapMessage(NetworkMessage):
    protocolId = 9325
    mapId:float
    mapKey:str
    
