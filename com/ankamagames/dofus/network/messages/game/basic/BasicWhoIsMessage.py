from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


class BasicWhoIsMessage(NetworkMessage):
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
    
