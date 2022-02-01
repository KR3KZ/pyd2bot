from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SimpleCharacterCharacteristicForPreset(INetworkMessage):
    protocolId = 7495
    keyword:str
    base:int
    additionnal:int
    
    
