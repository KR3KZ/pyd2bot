from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations
    


class GuildFactsMessage(NetworkMessage):
    infos:'GuildFactSheetInformations'
    creationDate:int
    nbTaxCollectors:int
    members:list['CharacterMinimalGuildPublicInformations']
    

    def init(self, infos:'GuildFactSheetInformations', creationDate:int, nbTaxCollectors:int, members:list['CharacterMinimalGuildPublicInformations']):
        self.infos = infos
        self.creationDate = creationDate
        self.nbTaxCollectors = nbTaxCollectors
        self.members = members
        
        super().__init__()
    
    