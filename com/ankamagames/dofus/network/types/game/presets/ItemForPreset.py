from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ItemForPreset(INetworkMessage):
    protocolId = 4107
    position:int
    objGid:int
    objUid:int
    
    
