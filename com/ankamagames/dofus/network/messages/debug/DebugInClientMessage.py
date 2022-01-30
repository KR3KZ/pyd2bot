from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DebugInClientMessage(NetworkMessage):
    protocolId = 6517
    level:int
    message:str
    
    
