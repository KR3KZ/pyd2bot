from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamLightInformations import FightTeamLightInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations


class FightExternalInformations(NetworkMessage):
    fightId:int
    fightType:int
    fightStart:int
    fightSpectatorLocked:bool
    fightTeams:list[FightTeamLightInformations]
    fightTeamsOptions:list[FightOptionsInformations]
    
    
