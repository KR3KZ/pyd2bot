from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AbstractPartyMessage(NetworkMessage):
    protocolId = 3299
    partyId:int
    
    
