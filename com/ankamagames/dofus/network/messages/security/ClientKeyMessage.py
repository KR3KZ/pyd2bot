from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ClientKeyMessage(NetworkMessage):
    protocolId = 7137
    key:str
    
