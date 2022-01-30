from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AdminCommandMessage(INetworkMessage):
    protocolId = 4583
    content:str
    
    
