from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations


class GuildFactsMessage(INetworkMessage):
    protocolId = 2464
    infos:GuildFactSheetInformations
    creationDate:int
    nbTaxCollectors:int
    members:CharacterMinimalGuildPublicInformations
    
    
