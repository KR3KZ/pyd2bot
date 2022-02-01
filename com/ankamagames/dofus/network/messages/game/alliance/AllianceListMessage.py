from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations


class AllianceListMessage(INetworkMessage):
    protocolId = 3861
    alliances:AllianceFactSheetInformations
    
    
