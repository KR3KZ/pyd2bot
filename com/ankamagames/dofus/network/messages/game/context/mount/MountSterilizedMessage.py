from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountSterilizedMessage(INetworkMessage):
    protocolId = 3777
    mountId:int
    
    
