from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SystemMessageDisplayMessage(INetworkMessage):
    protocolId = 4698
    hangUp:bool
    msgId:int
    parameters:str
    
    
