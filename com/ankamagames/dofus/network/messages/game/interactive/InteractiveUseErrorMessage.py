from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class InteractiveUseErrorMessage(INetworkMessage):
    protocolId = 778
    elemId:int
    skillInstanceUid:int
    
    
