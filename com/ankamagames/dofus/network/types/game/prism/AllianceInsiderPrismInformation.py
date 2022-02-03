from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class AllianceInsiderPrismInformation(PrismInformation):
    lastTimeSlotModificationDate:int
    lastTimeSlotModificationAuthorGuildId:int
    lastTimeSlotModificationAuthorId:int
    lastTimeSlotModificationAuthorName:str
    modulesObjects:list['ObjectItem']
    

    def init(self, lastTimeSlotModificationDate:int, lastTimeSlotModificationAuthorGuildId:int, lastTimeSlotModificationAuthorId:int, lastTimeSlotModificationAuthorName:str, modulesObjects:list['ObjectItem'], typeId:int, state:int, nextVulnerabilityDate:int, placementDate:int, rewardTokenCount:int):
        self.lastTimeSlotModificationDate = lastTimeSlotModificationDate
        self.lastTimeSlotModificationAuthorGuildId = lastTimeSlotModificationAuthorGuildId
        self.lastTimeSlotModificationAuthorId = lastTimeSlotModificationAuthorId
        self.lastTimeSlotModificationAuthorName = lastTimeSlotModificationAuthorName
        self.modulesObjects = modulesObjects
        
        super().__init__(typeId, state, nextVulnerabilityDate, placementDate, rewardTokenCount)
    
    