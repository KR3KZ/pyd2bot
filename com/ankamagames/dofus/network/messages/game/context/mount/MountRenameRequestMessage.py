from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountRenameRequestMessage(INetworkMessage):
    protocolId = 8042
    name:str
    mountId:int
    
    
