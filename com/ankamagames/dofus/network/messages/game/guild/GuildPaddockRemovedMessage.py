from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildPaddockRemovedMessage(NetworkMessage):
    protocolId = 9960
    paddockId:int
    
    
