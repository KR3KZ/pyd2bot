from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountFeedRequestMessage(NetworkMessage):
    mountUid:int
    mountLocation:int
    mountFoodUid:int
    quantity:int
    
    
