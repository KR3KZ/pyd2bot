from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.HavenBagFurnitureInformation import HavenBagFurnitureInformation


@dataclass
class HavenBagFurnituresMessage(NetworkMessage):
    furnituresInfos:list[HavenBagFurnitureInformation]
    
    
    def __post_init__(self):
        super().__init__()
    