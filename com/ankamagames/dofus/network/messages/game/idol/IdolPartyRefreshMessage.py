from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol
    


class IdolPartyRefreshMessage(NetworkMessage):
    partyIdol:'PartyIdol'
    

    def init(self, partyIdol:'PartyIdol'):
        self.partyIdol = partyIdol
        
        super().__init__()
    
    