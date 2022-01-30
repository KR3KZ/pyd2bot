from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class InvalidPresetsMessage(NetworkMessage):
    protocolId = 5030
    presetIds:list[int]
    
