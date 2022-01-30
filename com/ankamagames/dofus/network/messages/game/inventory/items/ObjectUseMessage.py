from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectUseMessage(INetworkMessage):
    protocolId = 3065
    objectUID:int
    
    
