from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntAvailableRetryCountUpdateMessage(NetworkMessage):
    questType:int
    availableRetryCount:int
    
    
