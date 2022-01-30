from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TitleSelectErrorMessage(INetworkMessage):
    protocolId = 2014
    reason:int
    
    
