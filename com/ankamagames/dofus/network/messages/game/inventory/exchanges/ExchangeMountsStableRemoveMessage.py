from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeMountsStableRemoveMessage(INetworkMessage):
    protocolId = 9668
    mountsId:int
    
    
