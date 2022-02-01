from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountInformationRequestMessage(INetworkMessage):
    protocolId = 2112
    id:int
    time:int
    
    
