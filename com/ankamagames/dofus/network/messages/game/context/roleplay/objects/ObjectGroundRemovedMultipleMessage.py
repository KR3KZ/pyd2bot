from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectGroundRemovedMultipleMessage(INetworkMessage):
    protocolId = 6993
    cells:int
    
    
