from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IconPresetSaveRequestMessage(NetworkMessage):
    presetId:int
    symbolId:int
    updateData:bool
    
    
