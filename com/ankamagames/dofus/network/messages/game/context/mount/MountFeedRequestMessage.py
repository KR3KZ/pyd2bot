from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountFeedRequestMessage(INetworkMessage):
    protocolId = 8131
    mountUid:int
    mountLocation:int
    mountFoodUid:int
    quantity:int
    
    
