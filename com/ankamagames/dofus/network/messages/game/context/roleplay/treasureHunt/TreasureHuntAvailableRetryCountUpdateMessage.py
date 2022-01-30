from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntAvailableRetryCountUpdateMessage(NetworkMessage):
    protocolId = 3416
    questType:int
    availableRetryCount:int
    
