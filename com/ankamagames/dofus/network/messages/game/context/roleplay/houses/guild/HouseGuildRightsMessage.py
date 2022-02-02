from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


@dataclass
class HouseGuildRightsMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    guildInfo:GuildInformations
    rights:int
    
    
    def __post_init__(self):
        super().__init__()
    