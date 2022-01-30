from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations


class AllianceListMessage(NetworkMessage):
    protocolId = 3861
    alliances:AllianceFactSheetInformations
    
