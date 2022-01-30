from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class HouseGuildRightsMessage(NetworkMessage):
    protocolId = 5258
    houseId:int
    instanceId:int
    secondHand:bool
    guildInfo:GuildInformations
    rights:int
    
