from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameActionFightCastRequestMessage(NetworkMessage):
    protocolId = 4946
    spellId:int
    cellId:int
    
