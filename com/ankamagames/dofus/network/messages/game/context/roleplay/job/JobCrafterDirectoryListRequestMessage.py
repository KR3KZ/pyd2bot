from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class JobCrafterDirectoryListRequestMessage(INetworkMessage):
    protocolId = 5786
    jobId:int
    
    
