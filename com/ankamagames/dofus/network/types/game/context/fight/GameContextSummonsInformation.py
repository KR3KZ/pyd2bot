from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation


class GameContextSummonsInformation(INetworkMessage):
    protocolId = 253
    spawnInformation:SpawnInformation
    wave:int
    look:EntityLook
    stats:GameFightCharacteristics
    summons:GameContextBasicSpawnInformation
    
    
