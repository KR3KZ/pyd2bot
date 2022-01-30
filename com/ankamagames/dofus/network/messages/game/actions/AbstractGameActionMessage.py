from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AbstractGameActionMessage(NetworkMessage):
    protocolId = 5037
    actionId:int
    sourceId:int
    
