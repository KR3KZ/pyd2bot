from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


@dataclass
class BreachInvitationResponseMessage(NetworkMessage):
    guest:CharacterMinimalInformations
    accept:bool
    
    
    def __post_init__(self):
        super().__init__()
    