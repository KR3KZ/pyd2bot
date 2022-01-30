from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SpouseStatusMessage(NetworkMessage):
    protocolId = 5406
    hasSpouse:bool
    
