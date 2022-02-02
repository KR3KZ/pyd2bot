from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


@dataclass
class GuildHouseUpdateInformationMessage(NetworkMessage):
    housesInformations:HouseInformationsForGuild
    
    
    def __post_init__(self):
        super().__init__()
    