from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterCreationRequestMessage(INetworkMessage):
    protocolId = 5026
    name:str
    breed:int
    sex:bool
    colors:list[int]
    cosmeticId:int
    
    
