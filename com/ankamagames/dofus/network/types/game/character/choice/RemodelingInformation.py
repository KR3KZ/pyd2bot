from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class RemodelingInformation(NetworkMessage):
    protocolId = 8002
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:int
    
    
