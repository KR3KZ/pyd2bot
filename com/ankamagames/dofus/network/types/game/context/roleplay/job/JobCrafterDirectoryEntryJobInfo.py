from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryJobInfo(NetworkMessage):
    jobId:int
    jobLevel:int
    free:bool
    minLevel:int
    
    
