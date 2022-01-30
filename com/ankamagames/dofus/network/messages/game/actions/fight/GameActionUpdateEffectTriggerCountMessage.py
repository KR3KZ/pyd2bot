from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


class GameActionUpdateEffectTriggerCountMessage(INetworkMessage):
    protocolId = 6461
    targetIds:GameFightEffectTriggerCount
    
    
