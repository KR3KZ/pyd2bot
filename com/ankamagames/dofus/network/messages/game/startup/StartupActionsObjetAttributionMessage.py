from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StartupActionsObjetAttributionMessage(INetworkMessage):
    protocolId = 8408
    actionId:int
    characterId:int
    
    
