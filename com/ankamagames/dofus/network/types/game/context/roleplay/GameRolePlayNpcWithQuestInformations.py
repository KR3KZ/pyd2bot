from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag


class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
    protocolId = 3824
    questFlag:GameRolePlayNpcQuestFlag
    
