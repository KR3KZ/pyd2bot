from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PresetDeleteRequestMessage(INetworkMessage):
    protocolId = 3688
    presetId:int
    
    
