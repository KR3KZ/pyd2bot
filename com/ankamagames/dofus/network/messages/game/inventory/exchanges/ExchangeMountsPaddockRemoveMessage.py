from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeMountsPaddockRemoveMessage(INetworkMessage):
    protocolId = 2113
    mountsId:int
    
    
