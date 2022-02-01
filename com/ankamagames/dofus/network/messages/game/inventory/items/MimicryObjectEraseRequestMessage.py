from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MimicryObjectEraseRequestMessage(INetworkMessage):
    protocolId = 3575
    hostUID:int
    hostPos:int
    
    
