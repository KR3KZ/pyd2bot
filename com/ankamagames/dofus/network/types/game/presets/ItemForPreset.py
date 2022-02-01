from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ItemForPreset(INetworkMessage):
    protocolId = 4107
    position:int
    objGid:int
    objUid:int
    
    
