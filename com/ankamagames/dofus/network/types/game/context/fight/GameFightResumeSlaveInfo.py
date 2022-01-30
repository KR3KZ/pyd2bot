from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown


class GameFightResumeSlaveInfo(NetworkMessage):
    protocolId = 8117
    slaveId:float
    spellCooldowns:list[GameFightSpellCooldown]
    summonCount:int
    bombCount:int
    
