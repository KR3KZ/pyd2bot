from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SimpleCharacterCharacteristicForPreset(NetworkMessage):
    protocolId = 7495
    keyword:str
    base:int
    additionnal:int
    
    
