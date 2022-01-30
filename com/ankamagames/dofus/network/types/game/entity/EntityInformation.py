from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EntityInformation(INetworkMessage):
    protocolId = 6041
    id:int
    experience:int
    status:bool
    
    
