from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StartupActionsAllAttributionMessage(INetworkMessage):
    protocolId = 2956
    characterId:int
    
    
