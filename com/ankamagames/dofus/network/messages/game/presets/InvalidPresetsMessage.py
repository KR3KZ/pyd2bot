from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class InvalidPresetsMessage(INetworkMessage):
    protocolId = 5030
    presetIds:int
    
    
