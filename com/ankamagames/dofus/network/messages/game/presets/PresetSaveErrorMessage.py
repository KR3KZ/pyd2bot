from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PresetSaveErrorMessage(INetworkMessage):
    protocolId = 2325
    presetId:int
    code:int
    
    
