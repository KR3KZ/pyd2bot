from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayMutantInformations(GameRolePlayHumanoidInformations):
    monsterId:int
    powerLevel:int
    

    def init(self, monsterId:int, powerLevel:int, humanoidInfo:'HumanInformations', accountId:int, name:str, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.monsterId = monsterId
        self.powerLevel = powerLevel
        
        super().__init__(humanoidInfo, accountId, name, look, contextualId, disposition)
    
    