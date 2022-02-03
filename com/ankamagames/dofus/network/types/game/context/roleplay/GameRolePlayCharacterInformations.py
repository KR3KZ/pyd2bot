from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayCharacterInformations(GameRolePlayHumanoidInformations):
    alignmentInfos:'ActorAlignmentInformations'
    

    def init(self, alignmentInfos:'ActorAlignmentInformations', humanoidInfo:'HumanInformations', accountId:int, name:str, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.alignmentInfos = alignmentInfos
        
        super().__init__(humanoidInfo, accountId, name, look, contextualId, disposition)
    
    