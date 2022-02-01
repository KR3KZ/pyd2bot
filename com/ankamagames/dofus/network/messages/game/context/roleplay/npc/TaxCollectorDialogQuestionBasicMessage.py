from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorDialogQuestionBasicMessage(INetworkMessage):
    protocolId = 1694
    guildInfo:BasicGuildInformations
    
    
