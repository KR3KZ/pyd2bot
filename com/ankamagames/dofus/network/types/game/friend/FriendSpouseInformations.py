from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


@dataclass
class FriendSpouseInformations(NetworkMessage):
    spouseAccountId:int
    spouseId:int
    spouseName:str
    spouseLevel:int
    breed:int
    sex:int
    spouseEntityLook:EntityLook
    guildInfo:GuildInformations
    alignmentSide:int
    
    
    def __post_init__(self):
        super().__init__()
    