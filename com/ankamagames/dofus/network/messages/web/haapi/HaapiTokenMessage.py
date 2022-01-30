from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiTokenMessage(NetworkMessage):
    protocolId = 8938
    token:str
    
