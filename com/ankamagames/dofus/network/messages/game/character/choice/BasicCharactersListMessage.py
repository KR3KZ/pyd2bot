from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


@dataclass
class BasicCharactersListMessage(NetworkMessage):
    characters:list[CharacterBaseInformations]
    
    
    def __post_init__(self):
        super().__init__()
    