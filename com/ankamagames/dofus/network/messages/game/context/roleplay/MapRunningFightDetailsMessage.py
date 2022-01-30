from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class MapRunningFightDetailsMessage(INetworkMessage):
    protocolId = 3380
    fightId:int
    attackers:GameFightFighterLightInformations
    defenders:GameFightFighterLightInformations
    
    
