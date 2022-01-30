from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations


class GameRolePlayShowChallengeMessage(NetworkMessage):
    protocolId = 5734
    commonsInfos:FightCommonInformations
    
