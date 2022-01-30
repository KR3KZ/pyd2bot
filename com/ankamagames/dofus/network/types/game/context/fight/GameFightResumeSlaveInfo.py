from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown


class GameFightResumeSlaveInfo(NetworkMessage):
    protocolId = 8117
    slaveId:int
    spellCooldowns:GameFightSpellCooldown
    summonCount:int
    bombCount:int
    
    
