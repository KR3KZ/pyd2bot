from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildCharacsUpgradeRequestMessage(NetworkMessage):
    protocolId = 3240
    charaTypeTarget:int
    
    
