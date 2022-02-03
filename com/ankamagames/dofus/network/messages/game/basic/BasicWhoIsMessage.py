from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos
    


class BasicWhoIsMessage(NetworkMessage):
    position:int
    accountTag:'AccountTagInformation'
    accountId:int
    playerName:str
    playerId:int
    areaId:int
    serverId:int
    originServerId:int
    socialGroups:list['AbstractSocialGroupInfos']
    playerState:int
    self:bool
    verbose:bool
    

    def init(self, position:int, accountTag:'AccountTagInformation', accountId:int, playerName:str, playerId:int, areaId:int, serverId:int, originServerId:int, socialGroups:list['AbstractSocialGroupInfos'], playerState:int):
        self.position = position
        self.accountTag = accountTag
        self.accountId = accountId
        self.playerName = playerName
        self.playerId = playerId
        self.areaId = areaId
        self.serverId = serverId
        self.originServerId = originServerId
        self.socialGroups = socialGroups
        self.playerState = playerState
        
        super().__init__()
    
    