from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.NpcDialogCreationMessage import NpcDialogCreationMessage


@dataclass
class PortalDialogCreationMessage(NpcDialogCreationMessage):
    type:int
    
    
    def __post_init__(self):
        super().__init__()
    