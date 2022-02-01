from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry


class JobCrafterDirectoryListMessage(INetworkMessage):
    protocolId = 7620
    listEntries:JobCrafterDirectoryListEntry
    
    
