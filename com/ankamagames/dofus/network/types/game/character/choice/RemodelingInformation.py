from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RemodelingInformation(NetworkMessage):
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:list[int]
    
    
