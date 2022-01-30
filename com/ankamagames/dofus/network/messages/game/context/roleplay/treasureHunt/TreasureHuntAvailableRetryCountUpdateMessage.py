from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntAvailableRetryCountUpdateMessage(INetworkMessage):
    protocolId = 3416
    questType:int
    availableRetryCount:int
    
    
