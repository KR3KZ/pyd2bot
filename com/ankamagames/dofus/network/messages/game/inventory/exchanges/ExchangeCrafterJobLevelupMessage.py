from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeCrafterJobLevelupMessage(INetworkMessage):
    protocolId = 6591
    crafterJobLevel:int
    
    
