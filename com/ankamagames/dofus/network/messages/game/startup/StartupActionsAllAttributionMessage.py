from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StartupActionsAllAttributionMessage(INetworkMessage):
    protocolId = 2956
    characterId:int
    
    
