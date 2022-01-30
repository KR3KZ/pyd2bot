from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HelloConnectMessage(NetworkMessage):
    protocolId = 6739
    salt:str
    key:int
    
