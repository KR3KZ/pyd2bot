from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.alignment.war.effort.AlignmentWarEffortInformation import AlignmentWarEffortInformation


@dataclass
class AlignmentWarEffortProgressionMessage(NetworkMessage):
    effortProgressions:list[AlignmentWarEffortInformation]
    
    
    def __post_init__(self):
        super().__init__()
    