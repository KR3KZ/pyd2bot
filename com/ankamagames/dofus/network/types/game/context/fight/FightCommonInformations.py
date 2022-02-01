from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations


class FightCommonInformations(NetworkMessage):
    fightId:int
    fightType:int
    fightTeams:list[FightTeamInformations]
    fightTeamsPositions:list[int]
    fightTeamsOptions:list[FightOptionsInformations]
    
    
