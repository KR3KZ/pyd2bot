from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PresetUseResultMessage(INetworkMessage):
    protocolId = 8808
    presetId:int
    code:int
    
    
