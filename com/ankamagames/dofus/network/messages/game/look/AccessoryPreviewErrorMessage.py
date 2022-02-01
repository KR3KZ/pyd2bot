from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AccessoryPreviewErrorMessage(INetworkMessage):
    protocolId = 2038
    error:int
    
    
