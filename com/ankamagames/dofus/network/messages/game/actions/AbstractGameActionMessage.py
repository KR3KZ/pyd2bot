from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AbstractGameActionMessage(INetworkMessage):
    protocolId = 5037
    actionId:int
    sourceId:int
    
    
