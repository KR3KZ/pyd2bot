from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundListAddedMessage(NetworkMessage):
    protocolId = 6617
    cells:int
    referenceIds:int
    
    
