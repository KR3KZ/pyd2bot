from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismSettingsRequestMessage(INetworkMessage):
    protocolId = 8342
    subAreaId:int
    startDefenseTime:int
    
    
