from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations


class GameRolePlayShowChallengeMessage(INetworkMessage):
    protocolId = 5734
    commonsInfos:FightCommonInformations
    
    
