from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PresetSaveErrorMessage(INetworkMessage):
    protocolId = 2325
    presetId:int
    code:int
    
    
