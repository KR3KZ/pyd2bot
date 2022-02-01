from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IconPresetSaveRequestMessage(INetworkMessage):
    protocolId = 4898
    presetId:int
    symbolId:int
    updateData:bool
    
    
