from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildCharacsUpgradeRequestMessage(INetworkMessage):
    protocolId = 3240
    charaTypeTarget:int
    
    
