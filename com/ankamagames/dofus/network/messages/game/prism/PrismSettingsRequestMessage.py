from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismSettingsRequestMessage(INetworkMessage):
    protocolId = 8342
    subAreaId:int
    startDefenseTime:int
    
    
