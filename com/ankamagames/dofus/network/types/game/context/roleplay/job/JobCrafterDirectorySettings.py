from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectorySettings(NetworkMessage):
    protocolId = 6079
    jobId:int
    minLevel:int
    free:bool
    
    
