from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo


class JobCrafterDirectoryListEntry(INetworkMessage):
    protocolId = 3897
    playerInfo:JobCrafterDirectoryEntryPlayerInfo
    jobInfo:JobCrafterDirectoryEntryJobInfo
    
    
