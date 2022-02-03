from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


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
    

    def init(self, maxPods:int, prospecting:int, wisdom:int, taxCollectorsCount:int, taxCollectorAttack:int, kamas:int, experience:int, pods:int, itemsValue:int, guildInfo:'BasicGuildInformations'):
        self.maxPods = maxPods
        self.prospecting = prospecting
        self.wisdom = wisdom
        self.taxCollectorsCount = taxCollectorsCount
        self.taxCollectorAttack = taxCollectorAttack
        self.kamas = kamas
        self.experience = experience
        self.pods = pods
        self.itemsValue = itemsValue
        
        super().__init__(guildInfo)
    
    