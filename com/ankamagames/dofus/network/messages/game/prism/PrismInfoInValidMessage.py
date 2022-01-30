from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismInfoInValidMessage(INetworkMessage):
    protocolId = 7307
    reason:int
    
    
