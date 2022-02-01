from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations


class GuildFactsMessage(NetworkMessage):
    infos:GuildFactSheetInformations
    creationDate:int
    nbTaxCollectors:int
    members:list[CharacterMinimalGuildPublicInformations]
    
    
