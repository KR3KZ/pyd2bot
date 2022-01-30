from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StartupActionsAllAttributionMessage(NetworkMessage):
    protocolId = 2956
    characterId:int
    
