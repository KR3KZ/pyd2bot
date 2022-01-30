from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SpouseStatusMessage(INetworkMessage):
    protocolId = 5406
    hasSpouse:bool
    
    
