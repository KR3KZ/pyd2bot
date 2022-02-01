from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry


class JobCrafterDirectoryAddMessage(INetworkMessage):
    protocolId = 1829
    listEntry:JobCrafterDirectoryListEntry
    
    
