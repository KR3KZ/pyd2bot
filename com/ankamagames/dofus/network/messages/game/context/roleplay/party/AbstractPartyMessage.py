from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AbstractPartyMessage(INetworkMessage):
    protocolId = 3299
    partyId:int
    
    
