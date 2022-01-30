from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class RemodelingInformation(INetworkMessage):
    protocolId = 8002
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:int
    
    
