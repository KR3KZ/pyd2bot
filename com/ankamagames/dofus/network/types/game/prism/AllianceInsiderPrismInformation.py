from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


@dataclass
class AllianceInsiderPrismInformation(PrismInformation):
    lastTimeSlotModificationDate:int
    lastTimeSlotModificationAuthorGuildId:int
    lastTimeSlotModificationAuthorId:int
    lastTimeSlotModificationAuthorName:str
    modulesObjects:list[ObjectItem]
    
    
    def __post_init__(self):
        super().__init__()
    