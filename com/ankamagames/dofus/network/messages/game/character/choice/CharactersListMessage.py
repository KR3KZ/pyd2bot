from com.ankamagames.dofus.network.messages.game.character.choice.BasicCharactersListMessage import BasicCharactersListMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
    


class CharactersListMessage(BasicCharactersListMessage):
    hasStartupActions:bool
    

    def init(self, hasStartupActions:bool, characters:list['CharacterBaseInformations']):
        self.hasStartupActions = hasStartupActions
        
        super().__init__(characters)
    
    