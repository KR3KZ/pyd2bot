from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.character.replay.CharacterReplayRequestMessage import CharacterReplayRequestMessage
from com.ankamagames.dofus.network.types.game.character.choice.RemodelingInformation import RemodelingInformation


@dataclass
class CharacterReplayWithRemodelRequestMessage(CharacterReplayRequestMessage):
    remodel:RemodelingInformation
    
    
    def __post_init__(self):
        super().__init__()
    