from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PresetDeleteResultMessage(INetworkMessage):
    protocolId = 7560
    presetId:int
    code:int
    
    
