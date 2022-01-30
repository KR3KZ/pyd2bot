from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


class GameActionUpdateEffectTriggerCountMessage(NetworkMessage):
    protocolId = 6461
    targetIds:list[GameFightEffectTriggerCount]
    
