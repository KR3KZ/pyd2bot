from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class HouseGuildRightsMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    guildInfo:'GuildInformations'
    rights:int
    

    def init(self, houseId:int, instanceId:int, secondHand:bool, guildInfo:'GuildInformations', rights:int):
        self.houseId = houseId
        self.instanceId = instanceId
        self.secondHand = secondHand
        self.guildInfo = guildInfo
        self.rights = rights
        
        super().__init__()
    
    