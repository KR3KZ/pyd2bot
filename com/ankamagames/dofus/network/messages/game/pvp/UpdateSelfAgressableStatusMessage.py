from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class UpdateSelfAgressableStatusMessage(NetworkMessage):
    protocolId = 4140
    status:int
    probationTime:int
    
    
