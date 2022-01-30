from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectUseMessage(NetworkMessage):
    protocolId = 3065
    objectUID:int
    
