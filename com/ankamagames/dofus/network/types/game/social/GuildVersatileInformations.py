from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildVersatileInformations(NetworkMessage):
    protocolId = 4170
    guildId:int
    leaderId:int
    guildLevel:int
    nbMembers:int
    
