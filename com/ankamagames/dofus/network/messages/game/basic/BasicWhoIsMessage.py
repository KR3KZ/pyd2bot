from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


class BasicWhoIsMessage(NetworkMessage):
    position:int
    accountTag:AccountTagInformation
    accountId:int
    playerName:str
    playerId:int
    areaId:int
    serverId:int
    originServerId:int
    socialGroups:list[AbstractSocialGroupInfos]
    playerState:int
    self:bool
    verbose:bool
    
    
