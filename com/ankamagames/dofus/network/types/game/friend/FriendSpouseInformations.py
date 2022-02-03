from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class FriendSpouseInformations(NetworkMessage):
    spouseAccountId:int
    spouseId:int
    spouseName:str
    spouseLevel:int
    breed:int
    sex:int
    spouseEntityLook:'EntityLook'
    guildInfo:'GuildInformations'
    alignmentSide:int
    

    def init(self, spouseAccountId:int, spouseId:int, spouseName:str, spouseLevel:int, breed:int, sex:int, spouseEntityLook:'EntityLook', guildInfo:'GuildInformations', alignmentSide:int):
        self.spouseAccountId = spouseAccountId
        self.spouseId = spouseId
        self.spouseName = spouseName
        self.spouseLevel = spouseLevel
        self.breed = breed
        self.sex = sex
        self.spouseEntityLook = spouseEntityLook
        self.guildInfo = guildInfo
        self.alignmentSide = alignmentSide
        
        super().__init__()
    
    