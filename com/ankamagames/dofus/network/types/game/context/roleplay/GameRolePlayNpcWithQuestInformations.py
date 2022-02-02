from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag


@dataclass
class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
    questFlag:GameRolePlayNpcQuestFlag
    
    
    def __post_init__(self):
        super().__init__()
    