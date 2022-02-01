from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PresetSaveErrorMessage(NetworkMessage):
    presetId:int
    code:int
    
    
