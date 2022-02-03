from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.alignment.war.effort.AlignmentWarEffortInformation import AlignmentWarEffortInformation
    


class AlignmentWarEffortProgressionMessage(NetworkMessage):
    effortProgressions:list['AlignmentWarEffortInformation']
    

    def init(self, effortProgressions:list['AlignmentWarEffortInformation']):
        self.effortProgressions = effortProgressions
        
        super().__init__()
    
    