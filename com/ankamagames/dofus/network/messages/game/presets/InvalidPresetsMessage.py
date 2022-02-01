from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class InvalidPresetsMessage(INetworkMessage):
    protocolId = 5030
    presetIds:int
    
    
