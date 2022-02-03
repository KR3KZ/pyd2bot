from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class HumanOptionAlliance(HumanOption):
    allianceInformations:'AllianceInformations'
    aggressable:int
    

    def init(self, allianceInformations:'AllianceInformations', aggressable:int):
        self.allianceInformations = allianceInformations
        self.aggressable = aggressable
        
        super().__init__()
    
    