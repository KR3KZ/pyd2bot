from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EntityInformation(INetworkMessage):
    protocolId = 6041
    id:int
    experience:int
    status:bool
    
    
