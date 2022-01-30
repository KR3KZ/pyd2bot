from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryRequestMessage(NetworkMessage):
    protocolId = 3858
    playerId:int
    
