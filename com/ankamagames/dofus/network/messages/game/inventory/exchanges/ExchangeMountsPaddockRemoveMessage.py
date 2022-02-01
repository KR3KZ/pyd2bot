from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeMountsPaddockRemoveMessage(INetworkMessage):
    protocolId = 2113
    mountsId:int
    
    
