from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SystemMessageDisplayMessage(NetworkMessage):
    protocolId = 4698
    hangUp:bool
    msgId:int
    parameters:str
    
