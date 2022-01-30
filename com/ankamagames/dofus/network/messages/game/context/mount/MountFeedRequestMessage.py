from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountFeedRequestMessage(NetworkMessage):
    protocolId = 8131
    mountUid:int
    mountLocation:int
    mountFoodUid:int
    quantity:int
    
    
