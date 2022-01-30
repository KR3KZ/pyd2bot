from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamLightInformations import FightTeamLightInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations


class FightExternalInformations(INetworkMessage):
    protocolId = 7149
    fightId:int
    fightType:int
    fightStart:int
    fightSpectatorLocked:bool
    fightTeams:list[FightTeamLightInformations]
    fightTeamsOptions:list[FightOptionsInformations]
    
    
