from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InvalidPresetsMessage(NetworkMessage):
    presetIds:list[int]
    
    
