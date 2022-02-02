from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


@dataclass
class GuildHousesInformationMessage(NetworkMessage):
    housesInformations:list[HouseInformationsForGuild]
    
    
    def __post_init__(self):
        super().__init__()
    