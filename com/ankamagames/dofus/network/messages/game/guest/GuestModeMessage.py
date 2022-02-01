from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuestModeMessage(INetworkMessage):
    protocolId = 9430
    active:bool
    
    
