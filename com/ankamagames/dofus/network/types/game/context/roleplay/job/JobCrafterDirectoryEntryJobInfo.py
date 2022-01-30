from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryJobInfo(NetworkMessage):
    protocolId = 5220
    jobId:int
    jobLevel:int
    free:bool
    minLevel:int
    
    
