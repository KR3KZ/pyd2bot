from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage


@dataclass
class EmotePlayMassiveMessage(EmotePlayAbstractMessage):
    actorIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    