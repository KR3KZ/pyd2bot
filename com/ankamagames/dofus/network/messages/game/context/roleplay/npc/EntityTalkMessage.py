from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EntityTalkMessage(INetworkMessage):
    protocolId = 4321
    entityId:int
    textId:int
    parameters:str
    
    
