from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class AllianceInsiderPrismInformation(PrismInformation):
    protocolId = 8201
    lastTimeSlotModificationDate:int
    lastTimeSlotModificationAuthorGuildId:int
    lastTimeSlotModificationAuthorId:int
    lastTimeSlotModificationAuthorName:str
    modulesObjects:ObjectItem
    
