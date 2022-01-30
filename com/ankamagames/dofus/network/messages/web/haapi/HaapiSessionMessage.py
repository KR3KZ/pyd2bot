from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiSessionMessage(NetworkMessage):
    protocolId = 5486
    key:str
    type:int
    
