from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IgnoredDeleteRequestMessage(NetworkMessage):
    protocolId = 2264
    accountId:int
    session:bool
    
