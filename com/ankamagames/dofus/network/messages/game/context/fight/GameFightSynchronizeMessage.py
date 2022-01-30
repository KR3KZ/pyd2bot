from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


class GameFightSynchronizeMessage(NetworkMessage):
    protocolId = 3028
    fighters:GameFightFighterInformations
    
    
