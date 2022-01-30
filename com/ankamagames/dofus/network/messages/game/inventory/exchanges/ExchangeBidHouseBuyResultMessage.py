from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseBuyResultMessage(INetworkMessage):
    protocolId = 3743
    uid:int
    bought:bool
    
    
