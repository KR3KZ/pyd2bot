from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class MapRunningFightDetailsMessage(NetworkMessage):
    protocolId = 3380
    fightId:int
    attackers:GameFightFighterLightInformations
    defenders:GameFightFighterLightInformations
    
