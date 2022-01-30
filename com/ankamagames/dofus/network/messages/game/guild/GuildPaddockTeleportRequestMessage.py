from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildPaddockTeleportRequestMessage(NetworkMessage):
    protocolId = 7914
    paddockId:int
    
    
