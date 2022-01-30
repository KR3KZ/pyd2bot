from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol


class IdolListMessage(NetworkMessage):
    protocolId = 9410
    chosenIdols:int
    partyChosenIdols:int
    partyIdols:PartyIdol
    
    
