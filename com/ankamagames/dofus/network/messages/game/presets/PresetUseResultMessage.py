from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PresetUseResultMessage(NetworkMessage):
    protocolId = 8808
    presetId:int
    code:int
    
