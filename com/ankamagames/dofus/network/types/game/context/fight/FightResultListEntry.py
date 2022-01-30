from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot


class FightResultListEntry(NetworkMessage):
    protocolId = 6627
    outcome:int
    wave:int
    rewards:FightLoot
    
    
