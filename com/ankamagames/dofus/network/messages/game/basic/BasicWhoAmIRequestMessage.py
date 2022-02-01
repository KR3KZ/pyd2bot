from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BasicWhoAmIRequestMessage(INetworkMessage):
    protocolId = 1281
    verbose:bool
    
    
