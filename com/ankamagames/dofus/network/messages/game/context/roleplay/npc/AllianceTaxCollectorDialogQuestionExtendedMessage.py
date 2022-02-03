from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionExtendedMessage import TaxCollectorDialogQuestionExtendedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class AllianceTaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionExtendedMessage):
    alliance:'BasicNamedAllianceInformations'
    

    def init(self, alliance:'BasicNamedAllianceInformations', maxPods:int, prospecting:int, wisdom:int, taxCollectorsCount:int, taxCollectorAttack:int, kamas:int, experience:int, pods:int, itemsValue:int, guildInfo:'BasicGuildInformations'):
        self.alliance = alliance
        
        super().__init__(maxPods, prospecting, wisdom, taxCollectorsCount, taxCollectorAttack, kamas, experience, pods, itemsValue, guildInfo)
    
    