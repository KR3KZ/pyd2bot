from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol


class IdolPartyRefreshMessage(INetworkMessage):
    protocolId = 7517
    partyIdol:PartyIdol
    
    
