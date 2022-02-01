from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EntityMovementInformations(INetworkMessage):
    protocolId = 7283
    id:int
    steps:int
    
    
