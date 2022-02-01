from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobCrafterDirectorySettings(INetworkMessage):
    protocolId = 6079
    jobId:int
    minLevel:int
    free:bool
    
    
