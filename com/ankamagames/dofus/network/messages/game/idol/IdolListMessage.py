from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol


class IdolListMessage(INetworkMessage):
    protocolId = 9410
    chosenIdols:int
    partyChosenIdols:int
    partyIdols:PartyIdol
    
    
