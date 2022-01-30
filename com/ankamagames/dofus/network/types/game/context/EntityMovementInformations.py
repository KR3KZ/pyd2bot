from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EntityMovementInformations(INetworkMessage):
    protocolId = 7283
    id:int
    steps:int
    
    
