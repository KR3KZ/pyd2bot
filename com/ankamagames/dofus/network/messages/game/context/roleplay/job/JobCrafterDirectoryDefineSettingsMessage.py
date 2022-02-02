from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings


@dataclass
class JobCrafterDirectoryDefineSettingsMessage(NetworkMessage):
    settings:JobCrafterDirectorySettings
    
    
    def __post_init__(self):
        super().__init__()
    