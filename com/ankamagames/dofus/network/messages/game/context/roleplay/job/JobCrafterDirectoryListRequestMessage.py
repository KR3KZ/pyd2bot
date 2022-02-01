from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobCrafterDirectoryListRequestMessage(INetworkMessage):
    protocolId = 5786
    jobId:int
    
    
