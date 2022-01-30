from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountInformationsForPaddock(INetworkMessage):
    protocolId = 1513
    modelId:int
    name:str
    ownerName:str
    
    
