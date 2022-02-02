from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.character.choice.BasicCharactersListMessage import BasicCharactersListMessage


@dataclass
class CharactersListMessage(BasicCharactersListMessage):
    hasStartupActions:bool
    
    
    def __post_init__(self):
        super().__init__()
    