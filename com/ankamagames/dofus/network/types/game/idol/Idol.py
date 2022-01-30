from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class Idol(NetworkMessage):
    protocolId = 960
    id:int
    xpBonusPercent:int
    dropBonusPercent:int
    
    
