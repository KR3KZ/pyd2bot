from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountInformationsForPaddock(NetworkMessage):
    protocolId = 1513
    modelId:int
    name:str
    ownerName:str
    
    
