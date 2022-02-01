from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ContactAddFailureMessage(INetworkMessage):
    protocolId = 7999
    reason:int
    
    
