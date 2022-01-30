from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryListRequestMessage(NetworkMessage):
    protocolId = 5786
    jobId:int
    
