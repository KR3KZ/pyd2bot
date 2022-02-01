from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismSubareaEmptyInfo(INetworkMessage):
    protocolId = 6884
    subAreaId:int
    allianceId:int
    
    
