from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


@dataclass
class GameRolePlayShowMultipleActorsMessage(NetworkMessage):
    informationsList:list[GameRolePlayActorInformations]
    
    
    def __post_init__(self):
        super().__init__()
    