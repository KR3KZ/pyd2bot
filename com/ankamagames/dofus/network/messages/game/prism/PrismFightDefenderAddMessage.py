from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    


class PrismFightDefenderAddMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    defender:'CharacterMinimalPlusLookInformations'
    

    def init(self, subAreaId:int, fightId:int, defender:'CharacterMinimalPlusLookInformations'):
        self.subAreaId = subAreaId
        self.fightId = fightId
        self.defender = defender
        
        super().__init__()
    
    