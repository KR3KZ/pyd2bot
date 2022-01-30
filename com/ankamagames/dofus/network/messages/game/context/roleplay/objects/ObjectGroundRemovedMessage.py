from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMessage(NetworkMessage):
    protocolId = 7554
    cell:int
    
    
