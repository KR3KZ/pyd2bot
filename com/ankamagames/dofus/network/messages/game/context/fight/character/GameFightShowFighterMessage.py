from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


class GameFightShowFighterMessage(NetworkMessage):
    protocolId = 2781
    informations:GameFightFighterInformations
    
    
