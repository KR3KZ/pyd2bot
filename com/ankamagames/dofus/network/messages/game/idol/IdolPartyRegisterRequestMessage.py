from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class IdolPartyRegisterRequestMessage(INetworkMessage):
    protocolId = 868
    register:bool
    
    
