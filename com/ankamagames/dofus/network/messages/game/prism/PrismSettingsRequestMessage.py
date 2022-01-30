from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismSettingsRequestMessage(NetworkMessage):
    protocolId = 8342
    subAreaId:int
    startDefenseTime:int
    
