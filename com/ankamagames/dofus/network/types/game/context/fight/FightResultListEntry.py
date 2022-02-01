from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot


class FightResultListEntry(NetworkMessage):
    outcome:int
    wave:int
    rewards:FightLoot
    
    
