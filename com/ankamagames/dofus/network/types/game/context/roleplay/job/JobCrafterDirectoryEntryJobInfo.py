from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class JobCrafterDirectoryEntryJobInfo(INetworkMessage):
    protocolId = 5220
    jobId:int
    jobLevel:int
    free:bool
    minLevel:int
    
    
