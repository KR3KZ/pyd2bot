from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class Idol(INetworkMessage):
    protocolId = 960
    id:int
    xpBonusPercent:int
    dropBonusPercent:int
    
    
