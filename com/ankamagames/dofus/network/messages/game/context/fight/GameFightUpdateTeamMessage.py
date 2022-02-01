from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations


class GameFightUpdateTeamMessage(INetworkMessage):
    protocolId = 9785
    fightId:int
    team:FightTeamInformations
    
    
