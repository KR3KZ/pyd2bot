from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class IdolPartyLostMessage(INetworkMessage):
    protocolId = 7502
    idolId:int
    
    
