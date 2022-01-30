from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismSubareaEmptyInfo(INetworkMessage):
    protocolId = 6884
    subAreaId:int
    allianceId:int
    
    
