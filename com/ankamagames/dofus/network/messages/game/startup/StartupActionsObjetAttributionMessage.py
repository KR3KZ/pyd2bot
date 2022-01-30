from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StartupActionsObjetAttributionMessage(NetworkMessage):
    protocolId = 8408
    actionId:int
    characterId:float
    
