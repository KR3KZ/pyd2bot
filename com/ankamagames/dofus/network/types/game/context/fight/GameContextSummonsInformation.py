from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation


@dataclass
class GameContextSummonsInformation(NetworkMessage):
    spawnInformation:SpawnInformation
    wave:int
    look:EntityLook
    stats:GameFightCharacteristics
    summons:list[GameContextBasicSpawnInformation]
    
    
    def __post_init__(self):
        super().__init__()
    