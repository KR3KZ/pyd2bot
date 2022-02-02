from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry


@dataclass
class JobCrafterDirectoryListMessage(NetworkMessage):
    listEntries:list[JobCrafterDirectoryListEntry]
    
    
    def __post_init__(self):
        super().__init__()
    