from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObtainedItemMessage(INetworkMessage):
    protocolId = 4201
    genericId:int
    baseQuantity:int
    
    
