from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
    questFlag:'GameRolePlayNpcQuestFlag'
    

    def init(self, questFlag:'GameRolePlayNpcQuestFlag', npcId:int, sex:bool, specialArtworkId:int, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.questFlag = questFlag
        
        super().__init__(npcId, sex, specialArtworkId, look, contextualId, disposition)
    
    