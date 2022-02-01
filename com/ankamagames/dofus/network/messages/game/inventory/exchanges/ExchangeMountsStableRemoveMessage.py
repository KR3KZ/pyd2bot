from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeMountsStableRemoveMessage(INetworkMessage):
    protocolId = 9668
    mountsId:int
    
    
