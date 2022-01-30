from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol


class IdolPartyRefreshMessage(NetworkMessage):
    protocolId = 7517
    partyIdol:PartyIdol
    
    
