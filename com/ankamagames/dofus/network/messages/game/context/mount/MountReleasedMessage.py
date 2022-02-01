from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountReleasedMessage(INetworkMessage):
    protocolId = 843
    mountId:int
    
    
