from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightJoinRequestMessage import GuildFightJoinRequestMessage


class GuildFightTakePlaceRequestMessage(GuildFightJoinRequestMessage):
    protocolId = 1932
    replacedCharacterId:float
    
