from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


@dataclass
class GuildFightPlayersHelpersJoinMessage(NetworkMessage):
    fightId:int
    playerInfo:CharacterMinimalPlusLookInformations
    
    
    def __post_init__(self):
        super().__init__()
    