from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol
    


class IdolListMessage(NetworkMessage):
    chosenIdols:list[int]
    partyChosenIdols:list[int]
    partyIdols:list['PartyIdol']
    

    def init(self, chosenIdols:list[int], partyChosenIdols:list[int], partyIdols:list['PartyIdol']):
        self.chosenIdols = chosenIdols
        self.partyChosenIdols = partyChosenIdols
        self.partyIdols = partyIdols
        
        super().__init__()
    
    