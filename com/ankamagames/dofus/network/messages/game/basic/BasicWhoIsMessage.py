from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


class BasicWhoIsMessage(INetworkMessage):
    protocolId = 7169
    position:int
    accountTag:AccountTagInformation
    accountId:int
    playerName:str
    playerId:int
    areaId:int
    serverId:int
    originServerId:int
    socialGroups:AbstractSocialGroupInfos
    playerState:int
    self:bool
    verbose:bool
    
    
