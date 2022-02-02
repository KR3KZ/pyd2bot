from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AnomalySubareaInformation import AnomalySubareaInformation


@dataclass
class AnomalySubareaInformationResponseMessage(NetworkMessage):
    subareas:list[AnomalySubareaInformation]
    
    
    def __post_init__(self):
        super().__init__()
    