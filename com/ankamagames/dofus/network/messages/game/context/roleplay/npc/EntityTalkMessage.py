from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EntityTalkMessage(INetworkMessage):
    protocolId = 4321
    entityId:int
    textId:int
    parameters:str
    
    
