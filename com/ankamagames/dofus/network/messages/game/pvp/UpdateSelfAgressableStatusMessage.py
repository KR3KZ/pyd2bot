from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class UpdateSelfAgressableStatusMessage(INetworkMessage):
    protocolId = 4140
    status:int
    probationTime:int
    
    
