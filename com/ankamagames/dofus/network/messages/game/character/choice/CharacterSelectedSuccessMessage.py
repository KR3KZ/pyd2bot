from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
    


class CharacterSelectedSuccessMessage(NetworkMessage):
    infos:'CharacterBaseInformations'
    isCollectingStats:bool
    

    def init(self, infos:'CharacterBaseInformations', isCollectingStats:bool):
        self.infos = infos
        self.isCollectingStats = isCollectingStats
        
        super().__init__()
    
    