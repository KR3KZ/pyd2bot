from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismSetSabotagedRefusedMessage(INetworkMessage):
    protocolId = 5200
    subAreaId:int
    reason:int
    
    
