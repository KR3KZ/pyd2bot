from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuestModeMessage(INetworkMessage):
    protocolId = 9430
    active:bool
    
    
