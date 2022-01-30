from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PresetDeleteRequestMessage(NetworkMessage):
    protocolId = 3688
    presetId:int
    
    
