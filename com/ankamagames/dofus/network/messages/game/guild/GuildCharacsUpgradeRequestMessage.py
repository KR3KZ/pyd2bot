from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildCharacsUpgradeRequestMessage(INetworkMessage):
    protocolId = 3240
    charaTypeTarget:int
    
    
