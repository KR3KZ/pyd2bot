from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismSubareaEmptyInfo(NetworkMessage):
    protocolId = 6884
    subAreaId:int
    allianceId:int
    
