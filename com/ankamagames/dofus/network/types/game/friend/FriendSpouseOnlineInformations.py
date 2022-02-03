from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class FriendSpouseOnlineInformations(FriendSpouseInformations):
    mapId:int
    subAreaId:int
    inFight:bool
    followSpouse:bool
    

    def init(self, mapId:int, subAreaId:int, spouseAccountId:int, spouseId:int, spouseName:str, spouseLevel:int, breed:int, sex:int, spouseEntityLook:'EntityLook', guildInfo:'GuildInformations', alignmentSide:int):
        self.mapId = mapId
        self.subAreaId = subAreaId
        
        super().__init__(spouseAccountId, spouseId, spouseName, spouseLevel, breed, sex, spouseEntityLook, guildInfo, alignmentSide)
    
    