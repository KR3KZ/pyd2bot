from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMultipleMessage(NetworkMessage):
    protocolId = 6993
    cells:int
    
    
