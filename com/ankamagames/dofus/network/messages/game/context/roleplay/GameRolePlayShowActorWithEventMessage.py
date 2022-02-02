from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.GameRolePlayShowActorMessage import GameRolePlayShowActorMessage


@dataclass
class GameRolePlayShowActorWithEventMessage(GameRolePlayShowActorMessage):
    actorEventId:int
    
    
    def __post_init__(self):
        super().__init__()
    