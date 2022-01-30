from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectGroundListAddedMessage(INetworkMessage):
    protocolId = 6617
    cells:int
    referenceIds:int
    
    
