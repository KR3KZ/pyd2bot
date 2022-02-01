from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobCrafterDirectoryEntryJobInfo(INetworkMessage):
    protocolId = 5220
    jobId:int
    jobLevel:int
    free:bool
    minLevel:int
    
    
