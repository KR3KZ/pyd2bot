from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class JobCrafterDirectoryEntryRequestMessage(INetworkMessage):
    protocolId = 3858
    playerId:int
    
    
