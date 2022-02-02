from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage


@dataclass
class TaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionBasicMessage):
    maxPods:int
    prospecting:int
    wisdom:int
    taxCollectorsCount:int
    taxCollectorAttack:int
    kamas:int
    experience:int
    pods:int
    itemsValue:int
    
    
    def __post_init__(self):
        super().__init__()
    