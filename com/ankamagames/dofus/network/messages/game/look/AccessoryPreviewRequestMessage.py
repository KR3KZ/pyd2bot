from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AccessoryPreviewRequestMessage(INetworkMessage):
    protocolId = 35
    genericId:int
    
    
