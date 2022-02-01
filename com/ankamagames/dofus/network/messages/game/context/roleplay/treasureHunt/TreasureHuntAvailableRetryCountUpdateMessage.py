from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntAvailableRetryCountUpdateMessage(INetworkMessage):
    protocolId = 3416
    questType:int
    availableRetryCount:int
    
    
