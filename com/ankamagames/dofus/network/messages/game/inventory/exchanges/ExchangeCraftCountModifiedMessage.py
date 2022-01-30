from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftCountModifiedMessage(NetworkMessage):
    protocolId = 2567
    count:int
    
    
