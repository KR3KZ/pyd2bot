from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionExtendedMessage import TaxCollectorDialogQuestionExtendedMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


class AllianceTaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionExtendedMessage):
    protocolId = 7917
    alliance:BasicNamedAllianceInformations
    
