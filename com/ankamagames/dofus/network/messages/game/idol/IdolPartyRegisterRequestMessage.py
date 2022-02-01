from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IdolPartyRegisterRequestMessage(INetworkMessage):
    protocolId = 868
    register:bool
    
    
