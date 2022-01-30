from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SimpleCharacterCharacteristicForPreset(INetworkMessage):
    protocolId = 7495
    keyword:str
    base:int
    additionnal:int
    
    
