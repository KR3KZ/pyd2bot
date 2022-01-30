from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PresetUseRequestMessage(NetworkMessage):
    protocolId = 1855
    presetId:int
    
    
