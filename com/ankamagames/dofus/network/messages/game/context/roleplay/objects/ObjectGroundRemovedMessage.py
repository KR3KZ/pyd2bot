from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectGroundRemovedMessage(INetworkMessage):
    protocolId = 7554
    cell:int
    
    
