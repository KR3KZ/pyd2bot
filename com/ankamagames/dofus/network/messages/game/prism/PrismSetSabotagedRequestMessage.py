from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismSetSabotagedRequestMessage(INetworkMessage):
    protocolId = 1746
    subAreaId:int
    
    
