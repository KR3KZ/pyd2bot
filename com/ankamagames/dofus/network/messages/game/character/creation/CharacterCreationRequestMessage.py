from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCreationRequestMessage(NetworkMessage):
    name:str
    breed:int
    sex:bool
    colors:list[int]
    cosmeticId:int
    
    
