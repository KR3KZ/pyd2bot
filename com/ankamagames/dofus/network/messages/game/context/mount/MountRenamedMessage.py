from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountRenamedMessage(INetworkMessage):
    protocolId = 7698
    mountId:int
    name:str
    
    
