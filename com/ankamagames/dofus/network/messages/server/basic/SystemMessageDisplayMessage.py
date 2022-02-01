from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SystemMessageDisplayMessage(INetworkMessage):
    protocolId = 4698
    hangUp:bool
    msgId:int
    parameters:str
    
    
