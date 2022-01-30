from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PresetDeleteResultMessage(NetworkMessage):
    protocolId = 7560
    presetId:int
    code:int
    
    
