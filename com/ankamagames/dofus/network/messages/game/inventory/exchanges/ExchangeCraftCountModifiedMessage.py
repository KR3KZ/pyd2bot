from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeCraftCountModifiedMessage(INetworkMessage):
    protocolId = 2567
    count:int
    
    
