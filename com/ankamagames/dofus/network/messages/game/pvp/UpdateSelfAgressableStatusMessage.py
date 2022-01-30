from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class UpdateSelfAgressableStatusMessage(INetworkMessage):
    protocolId = 4140
    status:int
    probationTime:int
    
    
