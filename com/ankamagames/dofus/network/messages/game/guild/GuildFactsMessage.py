from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations


class GuildFactsMessage(NetworkMessage):
    protocolId = 2464
    infos:GuildFactSheetInformations
    creationDate:int
    nbTaxCollectors:int
    members:list[CharacterMinimalGuildPublicInformations]
    
