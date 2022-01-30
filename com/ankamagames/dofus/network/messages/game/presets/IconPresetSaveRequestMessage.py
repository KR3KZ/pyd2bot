from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IconPresetSaveRequestMessage(NetworkMessage):
    protocolId = 4898
    presetId:int
    symbolId:int
    updateData:bool
    
