from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterCreationRequestMessage(NetworkMessage):
    protocolId = 5026
    name:str
    breed:int
    sex:bool
    colors:list[int]
    cosmeticId:int
    
    
