from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionExtendedMessage import TaxCollectorDialogQuestionExtendedMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


@dataclass
class AllianceTaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionExtendedMessage):
    alliance:BasicNamedAllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    