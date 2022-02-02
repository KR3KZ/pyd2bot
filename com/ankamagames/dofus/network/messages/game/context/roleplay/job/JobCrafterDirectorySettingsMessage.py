from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


@dataclass
class JobCrafterDirectorySettingsMessage(NetworkMessage):
    craftersSettings:list[JobCrafterDirectorySettings]
    
    
    def __post_init__(self):
        super().__init__()
    