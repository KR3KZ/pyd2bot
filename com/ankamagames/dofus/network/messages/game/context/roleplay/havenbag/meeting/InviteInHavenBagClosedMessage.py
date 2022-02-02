from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


@dataclass
class InviteInHavenBagClosedMessage(NetworkMessage):
    hostInformations:CharacterMinimalInformations
    
    
    def __post_init__(self):
        super().__init__()
    