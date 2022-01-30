from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PresetDeleteResultMessage(INetworkMessage):
    protocolId = 7560
    presetId:int
    code:int
    
    
