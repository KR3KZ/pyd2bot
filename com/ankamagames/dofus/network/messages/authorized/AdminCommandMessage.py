from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AdminCommandMessage(NetworkMessage):
    protocolId = 4583
    content:str
    
