from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ProtocolRequired(NetworkMessage):
    protocolId = 5716
    version:str
    
    
