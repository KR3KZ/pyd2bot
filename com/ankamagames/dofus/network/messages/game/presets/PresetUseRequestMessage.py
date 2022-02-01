from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PresetUseRequestMessage(INetworkMessage):
    protocolId = 1855
    presetId:int
    
    
