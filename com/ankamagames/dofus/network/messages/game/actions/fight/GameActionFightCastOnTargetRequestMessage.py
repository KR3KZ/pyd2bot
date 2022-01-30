from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameActionFightCastOnTargetRequestMessage(NetworkMessage):
    protocolId = 8001
    spellId:int
    targetId:float
    
