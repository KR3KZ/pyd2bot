from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class InteractiveUseRequestMessage(INetworkMessage):
    protocolId = 9714
    elemId:int
    skillInstanceUid:int
    
    
