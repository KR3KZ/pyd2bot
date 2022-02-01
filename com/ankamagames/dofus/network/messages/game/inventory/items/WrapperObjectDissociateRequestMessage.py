from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class WrapperObjectDissociateRequestMessage(INetworkMessage):
    protocolId = 9634
    hostUID:int
    hostPos:int
    
    
