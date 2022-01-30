from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DebugInClientMessage(INetworkMessage):
    protocolId = 6517
    level:int
    message:str
    
    
