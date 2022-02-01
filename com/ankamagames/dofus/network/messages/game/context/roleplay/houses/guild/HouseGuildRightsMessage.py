from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class HouseGuildRightsMessage(INetworkMessage):
    protocolId = 5258
    houseId:int
    instanceId:int
    secondHand:bool
    guildInfo:GuildInformations
    rights:int
    
    
