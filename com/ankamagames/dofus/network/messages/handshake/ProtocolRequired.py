from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ProtocolRequired(INetworkMessage):
    protocolId = 5716
    version:str
    
    
