from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations


class GameFightUpdateTeamMessage(NetworkMessage):
    protocolId = 9785
    fightId:int
    team:FightTeamInformations
    
