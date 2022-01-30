from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PresetUseResultMessage(INetworkMessage):
    protocolId = 8808
    presetId:int
    code:int
    
    
