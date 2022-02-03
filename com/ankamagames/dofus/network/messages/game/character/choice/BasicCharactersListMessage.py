from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
    


class BasicCharactersListMessage(NetworkMessage):
    characters:list['CharacterBaseInformations']
    

    def init(self, characters:list['CharacterBaseInformations']):
        self.characters = characters
        
        super().__init__()
    
    