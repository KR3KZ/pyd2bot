from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
    


class FightTeamMemberWithAllianceCharacterInformations(FightTeamMemberCharacterInformations):
    allianceInfos:'BasicAllianceInformations'
    

    def init(self, allianceInfos:'BasicAllianceInformations', name:str, level:int, id:int):
        self.allianceInfos = allianceInfos
        
        super().__init__(name, level, id)
    
    