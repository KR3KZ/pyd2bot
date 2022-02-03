from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    


class PrismFightAttackerAddMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    attacker:'CharacterMinimalPlusLookInformations'
    

    def init(self, subAreaId:int, fightId:int, attacker:'CharacterMinimalPlusLookInformations'):
        self.subAreaId = subAreaId
        self.fightId = fightId
        self.attacker = attacker
        
        super().__init__()
    
    