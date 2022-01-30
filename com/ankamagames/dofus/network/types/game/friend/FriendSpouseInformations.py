from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class FriendSpouseInformations(NetworkMessage):
    protocolId = 9956
    spouseAccountId:int
    spouseId:int
    spouseName:str
    spouseLevel:int
    breed:int
    sex:int
    spouseEntityLook:EntityLook
    guildInfo:GuildInformations
    alignmentSide:int
    
    
