from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountInformationsForPaddock(INetworkMessage):
    protocolId = 1513
    modelId:int
    name:str
    ownerName:str
    
    
