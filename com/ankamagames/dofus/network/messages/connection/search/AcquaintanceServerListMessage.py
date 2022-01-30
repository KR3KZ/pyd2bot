from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AcquaintanceServerListMessage(NetworkMessage):
    protocolId = 8752
    servers:int
    
    
