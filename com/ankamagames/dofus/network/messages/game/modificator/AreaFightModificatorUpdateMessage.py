from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AreaFightModificatorUpdateMessage(NetworkMessage):
    protocolId = 4779
    spellPairId:int
    
