from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyResultMessage(NetworkMessage):
    protocolId = 3743
    uid:int
    bought:bool
    
