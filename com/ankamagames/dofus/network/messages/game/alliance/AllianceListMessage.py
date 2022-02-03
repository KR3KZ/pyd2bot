from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
    


class AllianceListMessage(NetworkMessage):
    alliances:list['AllianceFactSheetInformations']
    

    def init(self, alliances:list['AllianceFactSheetInformations']):
        self.alliances = alliances
        
        super().__init__()
    
    