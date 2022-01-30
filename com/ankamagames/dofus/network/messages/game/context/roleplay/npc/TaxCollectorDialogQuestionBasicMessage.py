from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorDialogQuestionBasicMessage(NetworkMessage):
    protocolId = 1694
    guildInfo:BasicGuildInformations
    
