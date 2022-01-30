from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObtainedItemMessage(NetworkMessage):
    protocolId = 4201
    genericId:int
    baseQuantity:int
    
    
