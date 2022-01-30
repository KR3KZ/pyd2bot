from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeCrafterJobLevelupMessage(INetworkMessage):
    protocolId = 6591
    crafterJobLevel:int
    
    
