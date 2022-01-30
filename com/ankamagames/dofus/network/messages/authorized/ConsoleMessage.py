from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ConsoleMessage(NetworkMessage):
    protocolId = 3282
    type:int
    content:str
    
