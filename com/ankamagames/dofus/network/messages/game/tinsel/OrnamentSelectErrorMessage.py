from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class OrnamentSelectErrorMessage(NetworkMessage):
    protocolId = 4098
    reason:int
    
