from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.RemodelingInformation import RemodelingInformation
    


class CharacterSelectionWithRemodelMessage(CharacterSelectionMessage):
    remodel:'RemodelingInformation'
    

    def init(self, remodel:'RemodelingInformation', id:int):
        self.remodel = remodel
        
        super().__init__(id)
    
    