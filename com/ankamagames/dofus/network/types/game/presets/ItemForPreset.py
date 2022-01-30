from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ItemForPreset(NetworkMessage):
    protocolId = 4107
    position:int
    objGid:int
    objUid:int
    
