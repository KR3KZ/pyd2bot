from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations


class GameFightUpdateTeamMessage(INetworkMessage):
    protocolId = 9785
    fightId:int
    team:FightTeamInformations
    
    
