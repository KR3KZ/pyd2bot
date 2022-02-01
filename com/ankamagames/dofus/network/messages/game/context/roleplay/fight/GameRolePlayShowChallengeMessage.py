from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations


class GameRolePlayShowChallengeMessage(NetworkMessage):
    commonsInfos:FightCommonInformations
    
    
