from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations


class AllianceListMessage(NetworkMessage):
    alliances:list[AllianceFactSheetInformations]
    
    
