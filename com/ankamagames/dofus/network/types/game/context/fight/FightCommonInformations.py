from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations


class FightCommonInformations(NetworkMessage):
    protocolId = 5008
    fightId:int
    fightType:int
    fightTeams:FightTeamInformations
    fightTeamsPositions:int
    fightTeamsOptions:FightOptionsInformations
    
