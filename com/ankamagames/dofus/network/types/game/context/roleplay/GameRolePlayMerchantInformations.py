from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayMerchantInformations(GameRolePlayNamedActorInformations):
    sellType:int
    options:list['HumanOption']
    

    def init(self, sellType:int, options:list['HumanOption'], name:str, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.sellType = sellType
        self.options = options
        
        super().__init__(name, look, contextualId, disposition)
    
    