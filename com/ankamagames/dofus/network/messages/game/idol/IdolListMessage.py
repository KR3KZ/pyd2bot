from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol


class IdolListMessage(NetworkMessage):
    chosenIdols:list[int]
    partyChosenIdols:list[int]
    partyIdols:list[PartyIdol]
    
    
