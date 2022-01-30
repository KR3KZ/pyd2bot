from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StartupActionsObjetAttributionMessage(INetworkMessage):
    protocolId = 8408
    actionId:int
    characterId:int
    
    
