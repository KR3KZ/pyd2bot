from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayHumanoidInformations(GameRolePlayNamedActorInformations):
    humanoidInfo:'HumanInformations'
    accountId:int
    

    def init(self, humanoidInfo:'HumanInformations', accountId:int, name:str, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.humanoidInfo = humanoidInfo
        self.accountId = accountId
        
        super().__init__(name, look, contextualId, disposition)
    
    