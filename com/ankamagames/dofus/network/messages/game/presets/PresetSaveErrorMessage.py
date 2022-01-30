from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PresetSaveErrorMessage(NetworkMessage):
    protocolId = 2325
    presetId:int
    code:int
    
    
