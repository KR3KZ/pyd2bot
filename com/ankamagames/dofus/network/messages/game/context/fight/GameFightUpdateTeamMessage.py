from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations


class GameFightUpdateTeamMessage(NetworkMessage):
    fightId:int
    team:FightTeamInformations
    
    
